% File name: numerical_methods.m
% Author name: Troy Chin
% Version: 1.0
% Purpose: This script demonstrates solving linear ODEs using numerical
% methods including Euler's Method, Runge-Kutta (4th Order), and the Midpoint Method.

% =====================================================================
% NUMERICAL METHODS: Solving ODEs
% =====================================================================
disp('--- Solving ODEs Using Numerical Methods ---');

% Example ODE: y' = -2y, y(0) = -0.5
f = @(x, y) -2 * y;  % ODE function handle
h = 0.05;            % Step size
x = 0:h:5;           % x range
y_initial = -0.5;    % Initial condition

% =====================================================================
% EULER'S METHOD
% =====================================================================
disp('--- Euler''s Method ---');
[y_euler] = euler_method(f, x, y_initial);
disp('Euler''s Method Results:');
disp(table(x', y_euler', 'VariableNames', {'x', 'y'}));

% =====================================================================
% RUNGE-KUTTA METHOD (4th Order)
% =====================================================================
disp('--- Runge-Kutta Method (4th Order) ---');
[y_rk4] = runge_kutta_4(f, x, y_initial);
disp('Runge-Kutta 4th Order Results:');
disp(table(x', y_rk4', 'VariableNames', {'x', 'y'}));

% =====================================================================
% MIDPOINT METHOD
% =====================================================================
disp('--- Midpoint Method ---');
[y_midpoint] = midpoint_method(f, x, y_initial);
disp('Midpoint Method Results:');
disp(table(x', y_midpoint', 'VariableNames', {'x', 'y'}));

% =====================================================================
% PLOTTING RESULTS
% =====================================================================
figure;
plot(x, y_euler, '-o', 'DisplayName', 'Euler''s Method');
hold on;
plot(x, y_rk4, '-s', 'DisplayName', 'Runge-Kutta (4th Order)');
plot(x, y_midpoint, '-^', 'DisplayName', 'Midpoint Method');
xlabel('x');
ylabel('y');
title('Numerical Solutions to y'' = -2y, y(0) = -0.5');
legend show;
grid on;

% =====================================================================
% FUNCTION DEFINITIONS
% =====================================================================

% Euler's Method
function y = euler_method(f, x, y0)
    % Input: f - Function handle for ODE (dy/dx = f(x, y))
    %        x - Array of x values
    %        y0 - Initial condition y(x=0)
    % Output: y - Numerical solution for each x
    
    y = zeros(1, length(x));
    y(1) = y0;
    h = x(2) - x(1);  % Step size
    for i = 1:(length(x) - 1)
        y(i + 1) = y(i) + h * f(x(i), y(i));  % Euler formula
    end
end

% Runge-Kutta Method (4th Order)
function y = runge_kutta_4(f, x, y0)
    % Input: f - Function handle for ODE
    %        x - Array of x values
    %        y0 - Initial condition
    % Output: y - Numerical solution for each x
    
    y = zeros(1, length(x));
    y(1) = y0;
    h = x(2) - x(1);  % Step size
    for i = 1:(length(x) - 1)
        k1 = h * f(x(i), y(i));
        k2 = h * f(x(i) + h/2, y(i) + k1/2);
        k3 = h * f(x(i) + h/2, y(i) + k2/2);
        k4 = h * f(x(i) + h, y(i) + k3);
        y(i + 1) = y(i) + (k1 + 2*k2 + 2*k3 + k4) / 6;  % RK4 formula
    end
end

% Midpoint Method
function y = midpoint_method(f, x, y0)
    % Input: f - Function handle for ODE
    %        x - Array of x values
    %        y0 - Initial condition
    % Output: y - Numerical solution for each x
    
    y = zeros(1, length(x));
    y(1) = y0;
    h = x(2) - x(1);  % Step size
    for i = 1:(length(x) - 1)
        k1 = h * f(x(i), y(i));
        k2 = h * f(x(i) + h/2, y(i) + k1/2);
        y(i + 1) = y(i) + k2;  % Midpoint formula
    end
end


