% File name: numerical_methods.m
% Author name: Troy Chin (CWID: 885586685)
% Version: 1.6
% Purpose: Solve ODEs using different numerical methods, output solutions in the terminal, and plot them.

% ====================================================================
% PART 1: Solving Differential Equations using Euler's Method
% ====================================================================
function y = euler_method(func, y0, h)
    dydt = func(0, y0);
    y = y0 + h * dydt;
end

% ====================================================================
% PART 2: Solving Differential Equations using Runge-Kutta Method (RK4)
% ====================================================================
function y = runge_kutta(func, y0, h)
    k1 = func(0, y0);
    k2 = func(0, y0 + 0.5 * h * k1);
    k3 = func(0, y0 + 0.5 * h * k2);
    k4 = func(0, y0 + h * k3);

    y = y0 + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4);
end

% ====================================================================
% PART 3: Solving Differential Equations using Midpoint Method
% ====================================================================
function y = midpoint_method(func, y0, h)
    k1 = func(0, y0);
    y_mid = y0 + 0.5 * h * k1;
    k2 = func(0, y_mid);

    y = y0 + h * k2;
end

% ====================================================================
% MAIN: Solve ODE using different methods, output solutions, and plot them
% ====================================================================
function main()
    % Define the ODE: dy/dt = 3 * y
    func = @(t, y) 3 * y;

    % Parameters
    y0 = 2;        % Initial condition
    h = 0.1;       % Step size
    n_steps = 10;  % Number of time steps
    t = 0:h:(n_steps * h);  % Time vector

    % Initialize solution arrays
    y_euler = zeros(1, n_steps + 1);
    y_rk = zeros(1, n_steps + 1);
    y_mid = zeros(1, n_steps + 1);
    
    % Set initial conditions
    y_euler(1) = y0;
    y_rk(1) = y0;
    y_mid(1) = y0;

    % Solve using each method
    for i = 1:n_steps
        y_euler(i + 1) = euler_method(func, y_euler(i), h);
        y_rk(i + 1) = runge_kutta(func, y_rk(i), h);
        y_mid(i + 1) = midpoint_method(func, y_mid(i), h);
    end

    % Display results in the terminal
    disp('Numerical solutions for dy/dt = 3y:');
    disp('-----------------------------------');
    disp(' Time      Euler       RK4      Midpoint ');
    for i = 1:length(t)
        fprintf('%6.2f   %8.4f   %8.4f   %8.4f\n', t(i), y_euler(i), y_rk(i), y_mid(i));
    end

    % Plot the solutions
    figure;
    plot(t, y_euler, 'r--', 'LineWidth', 1.5); hold on;
    plot(t, y_rk, 'b-', 'LineWidth', 1.5);
    plot(t, y_mid, 'g-.', 'LineWidth', 1.5);

    % Customize the plot
    title('Numerical Solutions for dy/dt = 3y');
    xlabel('Time (t)');
    ylabel('Solution (y)');
    legend('Euler Method', 'Runge-Kutta Method (RK4)', 'Midpoint Method');
    grid on;
end

% Call the main function
main();
