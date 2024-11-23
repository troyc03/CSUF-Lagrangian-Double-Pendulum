% Numerical Integration/Differentiation Test Script
% This script tests the numerical_methods function.

% Define the function for differentiation
f = @(x) sin(x); % Function handle
x = pi / 4;      % Evaluation point
toler = 1e-5;    % Tolerance

% Call the function
[L, n] = numerical_methods(f, x, toler);

% Display results
disp('Step Sizes, Derivatives, and Errors:');
disp(L);
disp(['Number of Iterations: ', num2str(n)]);

% Function definition
function [L, n] = numerical_methods(f, x, toler)
    % Input - f: Function handle (e.g., @(x) x^2)
    %         x: Point of differentiation
    %         toler: Tolerance for error
    
    % Output - L = [H', D', E']
    %          H: Step sizes
    %          D: Approximate derivatives
    %          E: Error bounds

    max1 = 15; % Maximum iterations
    h = 1; % Initial step size
    H(1) = h;
    D(1) = (f(x + h) - f(x - h)) / (2 * h); % Central difference method
    E(1) = 0; % Initial error
    R(1) = 0; % Initial relative error

    for n = 1:2
        h = h / 10;
        H(n + 1) = h;
        D(n + 1) = (f(x + h) - f(x - h)) / (2 * h);
        E(n + 1) = abs(D(n + 1) - D(n));
        R(n + 1) = 2 * E(n + 1) / (abs(D(n + 1)) + abs(D(n)) + eps);
    end

    n = 2;
    while (E(n) > E(n + 1)) && (R(n) > toler) && (n < max1)
        h = h / 10;
        H(n + 2) = h;
        D(n + 2) = (f(x + h) - f(x - h)) / (2 * h);
        E(n + 2) = abs(D(n + 2) - D(n + 1));
        R(n + 2) = 2 * E(n + 2) / (abs(D(n + 2)) + abs(D(n + 1)) + eps);
        n = n + 1;
    end

    n = length(D) - 1;
    L = [H', D', E']; % Combine results into output
end
