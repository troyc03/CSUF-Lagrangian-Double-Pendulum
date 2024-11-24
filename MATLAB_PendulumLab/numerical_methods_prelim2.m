% File name: numerical_methods_prelim2.m
% Author name: Troy Chin
% Version: 1.1
% Purpose: This file provides a preliminary course in numerical
% differentiation and integration. It introduces fundamental methods:
% the Trapezoidal Rule, Simpson's Rule, and the Midpoint Rule.

% =====================================================================
% NUMERICAL INTEGRATION (Part 1): Trapezoidal Rule
% =====================================================================

% Example 1: Trapezoidal Rule
f1 = @(x) x^2 + 3*x + 4; % Define the function
a1 = 1;                 % Lower limit
b1 = 1.5;               % Upper limit
M1 = 4;                 % Number of subintervals

disp('--- Trapezoidal Rule ---');
disp('Evaluated integral of f(x) using Trapezoidal Rule:');
s1 = traprl(f1, a1, b1, M1);
disp(['Result: ', num2str(s1)]);

% Trapezoidal Rule Function
function s = traprl(f, a, b, M)
    h = (b - a) / M; % Step size
    s = 0;
    for k = 1:(M - 1)
        x = a + h * k;
        s = s + f(x); % Sum interior points
    end
    s = h * (f(a) + f(b)) / 2 + h * s; % Combine with boundary points
end

% =====================================================================
% NUMERICAL INTEGRATION (Part 2): Simpson’s Rule
% =====================================================================

% Example 2: Simpson's Rule
f2 = @(x) x^4 + 3*x^3 + 2*x^2 + x + 1; % Define the function
a2 = 2;                               % Lower limit
b2 = 3;                               % Upper limit
M2 = 2;                               % Number of subintervals (must be even)

disp('--- Simpson''s Rule ---');
disp('Evaluated integral of f(x) using Simpson''s Rule:');
s2 = simprl(f2, a2, b2, M2);
disp(['Result: ', num2str(s2)]);

% Simpson’s Rule Function
function s = simprl(f, a, b, M)
    if mod(M, 2) ~= 0
        error('Simpson''s Rule requires an even number of subintervals.');
    end
    h = (b - a) / (2 * M); % Step size
    s1 = 0; % Sum for odd terms
    s2 = 0; % Sum for even terms
    for k = 1:M
        x = a + h * (2 * k - 1); % Odd points
        s1 = s1 + f(x);
    end
    for k = 1:(M - 1)
        x = a + h * 2 * k; % Even points
        s2 = s2 + f(x);
    end
    s = (h / 3) * (f(a) + f(b) + 4 * s1 + 2 * s2); % Final formula
end

% =====================================================================
% NUMERICAL INTEGRATION (Part 3): Midpoint Rule
% =====================================================================

% Example 3: Midpoint Rule
f3 = @(x) sin(x);   % Define the function
a3 = 0;             % Lower limit
b3 = pi;            % Upper limit
M3 = 10;            % Number of subintervals

disp('--- Midpoint Rule ---');
disp('Evaluated integral of f(x) using Midpoint Rule:');
s3 = midpointrl(f3, a3, b3, M3);
disp(['Result: ', num2str(s3)]);

% Midpoint Rule Function
function s = midpointrl(f, a, b, M)
    h = (b - a) / M; % Step size
    s = 0;
    for k = 0:(M - 1)
        x_mid = a + h * (k + 0.5); % Midpoint
        s = s + f(x_mid);
    end
    s = h * s; % Final formula
end

% =====================================================================
% Conclusion
% =====================================================================
% This script demonstrates the three fundamental rules for numerical
% integration: the Trapezoidal Rule, Simpson's Rule, and the Midpoint Rule.
% Users can define their own functions, limits, and subintervals to
% experiment further.
