% File name: numerical_methods_prelim.m
% Author: Troy Chin
% Version: 1.2
% Purpose: This script provides a comprehensive introduction to numerical
% differentiation, focusing on finite differences and extrapolation methods.

% =====================================================================
% NUMERICAL DIFFERENTIATION PART 1a: Central Difference Method
% =====================================================================
disp('--- Numerical Differentiation: Central Difference ---');

% Example: Central Difference Approximation
f_central = @(x) sin(x);  % Function handle
x_central = pi / 4;       % Point of differentiation
tolerance = 1e-5;         % Tolerance for relative error

% Compute derivatives using central difference
[central_results, central_iters] = central_difference(f_central, x_central, tolerance);

% Display results
disp('Central Difference Results (Step Sizes, Derivatives, Errors):');
disp(central_results);
disp(['Number of Iterations: ', num2str(central_iters)]);

% Function for Central Difference
function [results, n] = central_difference(f, x, tolerance)
    % Input: f - Function handle
    %        x - Point of differentiation
    %        tolerance - Error tolerance
    % Output: results - Table [Step Sizes, Derivatives, Errors]
    %         n - Number of iterations

    max_iter = 15;  % Maximum iterations
    h = 1;          % Initial step size
    derivatives = []; errors = []; step_sizes = []; % Initialize arrays

    % Initial derivative calculation
    derivatives(1) = (f(x + h) - f(x - h)) / (2 * h);
    step_sizes(1) = h;
    errors(1) = 0;  % Initial error

    n = 1; % Iteration counter
    while n < max_iter
        % Update step size
        h = h / 10;
        step_sizes(n + 1) = h;

        % Compute new derivative
        new_derivative = (f(x + h) - f(x - h)) / (2 * h);
        derivatives(n + 1) = new_derivative;

        % Calculate error
        errors(n + 1) = abs(derivatives(n + 1) - derivatives(n));

        % Stop if relative error meets tolerance
        rel_error = 2 * errors(n + 1) / (abs(derivatives(n + 1)) + abs(derivatives(n)) + eps);
        if rel_error <= tolerance
            break;
        end

        n = n + 1;
    end

    % Combine results into table
    results = [step_sizes', derivatives', errors'];
end

% =====================================================================
% NUMERICAL DIFFERENTIATION PART 1b: Forward and Backward Differences
% =====================================================================
disp('--- Numerical Differentiation: Forward and Backward Differences ---');

% Example: Forward Difference
f_forward = @(x) exp(x);  % Function handle
x_forward = 2;            % Point of differentiation
h_forward = 0.1;          % Step size

forward_approx = finite_difference(f_forward, x_forward, h_forward, "forward");
disp(['Forward Difference Approximation at x = ', num2str(x_forward), ':']);
disp(forward_approx);

% Example: Backward Difference
backward_approx = finite_difference(f_forward, x_forward, h_forward, "backward");
disp(['Backward Difference Approximation at x = ', num2str(x_forward), ':']);
disp(backward_approx);

% Generalized Function for Forward/Backward Differences
function df = finite_difference(f, x, h, method)
    % Input: f - Function handle
    %        x - Point of differentiation
    %        h - Step size
    %        method - "forward" or "backward"
    % Output: df - Approximation of the derivative

    switch method
        case "forward"
            df = (f(x + h) - f(x)) / h;  % Forward difference formula
        case "backward"
            df = (f(x) - f(x - h)) / h;  % Backward difference formula
        otherwise
            error('Invalid method. Use "forward" or "backward".');
    end
end

% =====================================================================
% NUMERICAL DIFFERENTIATION PART 2: Extrapolation Method
% =====================================================================
disp('--- Numerical Differentiation: Extrapolation ---');

% Example 2: Extrapolation Method
f2 = @(x) cos(tan(1 / (1 + 2 * x))); % Function handle
x2 = 1 + sqrt(5) / 3;                % Point of differentiation
delta2 = 1e-5;                       % Minimum error
toler2 = 1e-5;                       % Tolerance

% Call the extrapolation function
[D2, err2, relerr2, n2] = diffext(f2, x2, delta2, toler2);

% Display results
disp('Extrapolated Derivatives, Errors, and Relative Errors:');
disp(D2);
disp(['Number of Iterations: ', num2str(n2)]);

% Function for extrapolation
function [D, err, relerr, n] = diffext(f, x, delta, toler)
    % Input: f - Function handle
    %        x - Point of differentiation
    %        delta - Minimum allowable error
    %        toler - Error tolerance
    % Output: D - Matrix of extrapolated derivatives
    %         err - Final error
    %         relerr - Final relative error
    %         n - Number of iterations

    err = 1;       % Initial error
    relerr = 1;    % Initial relative error
    h = 1;         % Initial step size
    j = 1;         % Iteration counter

    % Initial derivative (central difference)
    D(1, 1) = (f(x + h) - f(x - h)) / (2 * h);

    % Extrapolation iterations
    while err > delta && relerr > toler && j < 12
        % Reduce step size
        h = h / 2;
        D(j + 1, 1) = (f(x + h) - f(x - h)) / (2 * h);

        % Extrapolate results
        for k = 1:j
            D(j + 1, k + 1) = D(j + 1, k) + (D(j + 1, k) - D(j, k)) / (4^k - 1);
        end

        % Calculate error and relative error
        err = abs(D(j + 1, j + 1) - D(j, j));
        relerr = 2 * err / (abs(D(j + 1, j + 1)) + abs(D(j, j)) + eps);

        j = j + 1; % Increment iteration counter
    end

    n = size(D, 1); % Total iterations
end

% =====================================================================
% Conclusion
% =====================================================================
% This script demonstrates two methods for numerical differentiation:
% 1. Finite Differences (Forward, Backward, and Central).
% 2. Extrapolation techniques for improved accuracy.
% Users can define custom functions, points, and tolerances for testing.
