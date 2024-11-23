% PRELIMINARY: Numerical Integration/Differentiation 

% In order to understand numerical methods of solving differential
% equations, we must become familiar with numerical integration and
% differentiation. Let's begin with numerical differentiation using 
% the forward, backward, and central finite differences. 

% NUMERICAL DIFFERENTIATION PART 1: Numerical differentiation with limits

f = @(x) sin(x);  % Function handle
x = pi / 4;                  % Evaluation point
toler = 1e-5;                        % Tolerance

% Call the function
[L, n] = numerical_methods(f, x, toler);

% Display results
disp('Step Sizes, Derivatives, and Errors:');
disp(L);
disp(['Number of Iterations: ', num2str(n)]);

% Function definition for numerical differentiation with limits
function [L, n] = numerical_methods(f, x, toler)
    % f: Function handle (e.g., @(x) x^2)
    % x: Point of differentiation
    % toler: Tolerance for error

    max_iter = 15;  % Maximum iterations
    h = 1;          % Initial step size
    H = h;          % Step sizes array
    D = (f(x + h) - f(x - h)) / (2 * h);  % Central difference approximation
    E = 0;          % Initial error
    R = 0;          % Initial relative error
    
    % Initialize arrays for errors and relative errors
    errors = E;   
    rel_errors = R;
    derivatives = D;
    step_sizes = H;

    n = 1; % Iteration counter
    while (n < max_iter) && (n < length(errors)) && (errors(n) > errors(n + 1)) && (rel_errors(n) > toler)
        h = h / 10;  % Reduce step size
        step_sizes(n + 1) = h;
        
        % Compute new derivative using central difference
        D_new = (f(x + h) - f(x - h)) / (2 * h);
        derivatives(n + 1) = D_new;
        
        % Calculate error and relative error
        errors(n + 1) = abs(derivatives(n + 1) - derivatives(n));
        rel_errors(n + 1) = 2 * errors(n + 1) / (abs(derivatives(n + 1)) + abs(derivatives(n)) + eps);
        
        n = n + 1;
    end

    % Prepare output
    L = [step_sizes', derivatives', errors'];  % Combine results into output
end

% NUMERICAL DIFFERENTIATION PART 2: Numerical differentiation using extrapolation

f = @(x) cos(tan(1/(1 + x * 2)));  % Function handle
x = 1 + sqrt(5)/3;                  % Evaluation point
delta = 1e-5;                        % Minimum error for stopping
toler = 1e-5;                        % Tolerance

% Call the function
[D, err, relerr, n] = diffext(f, x, delta, toler);

% Display results
disp('Extrapolated Derivatives, Errors, and Relative Errors:');
disp(D);
disp(['Number of Iterations: ', num2str(n)]);

% Function definition for numerical differentiation using extrapolation
function [D, err, relerr, n] = diffext(f, x, delta, toler)
    % f: Function handle
    % x: Point of differentiation
    % delta: Minimum error for stopping
    % toler: Tolerance for relative error
    
    err = 1;
    relerr = 1;
    h = 1;  % Initial step size
    j = 1;  % Iteration counter
    
    % Initial derivative using central difference
    D(1, 1) = (feval(f, x + h) - feval(f, x - h)) / (2 * h);

    % Start iterations for extrapolation
    while relerr > toler && err > delta && j < 12
        h = h / 2;  % Reduce step size
        D(j + 1, 1) = (feval(f, x + h) - feval(f, x - h)) / (2 * h);  % New central difference
        
        % Extrapolate results
        for k = 1:j
            D(j + 1, k + 1) = D(j + 1, k) + (D(j + 1, k) - D(j, k)) / (4^k - 1);
        end
        
        % Calculate error and relative error
        err = abs(D(j + 1, j + 1) - D(j, j));
        relerr = 2 * err / (abs(D(j + 1, j + 1)) + abs(D(j, j)) + eps);
        
        % Increment iteration counter
        j = j + 1;
    end
    
    n = size(D, 1);  % Get the number of iterations
end


