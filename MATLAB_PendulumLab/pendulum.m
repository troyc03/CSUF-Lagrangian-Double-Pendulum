% File name: pendulum.m
% Author: Troy Chin
% Date: 15 November 2024
% Version: 1.0
% Purpose: Reimplementation of the Double Pendulum Lab in MATLAB with animation

% Define necessary parameters
m1 = 1.0; % mass1
m2 = 1.0; % mass2
l1 = 1.0; % length1
l2 = 1.0; % length2
g = 9.81; % Gravitational constant

% Define initial conditions
theta_1 = pi/4; % angle1
theta_2 = pi/6; % angle2
theta_dot1 = 0.0; % velocity1
theta_dot2 = 0.0; % velocity2

% Time span and step size
t_span = [0 5]; % Time from 0 to 20 seconds
dt = 0.01; % Time step
time = t_span(1):dt:t_span(2); % Time array

% Initial conditions for the system
y0 = [theta_1, theta_dot1, theta_2, theta_dot2]; % Initial state vector

% Define the system of differential equations (Euler-Lagrange equations)
% Equations for first and second pendulum
eqns = @(t, y) [
    y(2);
    (-g*(2*m1+m2)*sin(y(1)) - m2*g*sin(y(1)-2*y(3)) - 2*sin(y(1)-y(3))*m2*(y(4)^2*l2 + y(2)^2*l1*cos(y(1)-y(3))))/(l1*(2*m1+m2-m2*cos(2*y(1)-2*y(3)))); 
    y(4);
    (2*sin(y(1)-y(3))*(y(2)^2*l1*(m1+m2) + g*(m1+m2)*cos(y(1)) + y(4)^2*l2*m2*cos(y(1)-y(3))))/(l2*(2*m1+m2-m2*cos(2*y(1)-2*y(3))));
];

% Solve the system using ode45
[time, sol] = ode45(eqns, time, y0);

% Extract positions from the solution
theta1 = sol(:,1);
theta2 = sol(:,3);

% Calculate x and y positions of the masses
x1 = l1 * sin(theta1); % x position of mass 1
y1 = -l1 * cos(theta1); % y position of mass 1
x2 = x1 + l2 * sin(theta2); % x position of mass 2
y2 = y1 - l2 * cos(theta2); % y position of mass 2

% Set up the figure for animation
figure;
axis equal; % Ensure equal scaling on both axes
xlim([-2, 2]); % Adjust limits based on your pendulum's motion
ylim([-2, 2]);
hold on;

% Initial plot of the pendulum components
rod1 = line([0, x1(1)], [0, y1(1)], 'LineWidth', 2, 'Color', 'r'); % First rod
rod2 = line([x1(1), x2(1)], [y1(1), y2(1)], 'LineWidth', 2, 'Color', 'b'); % Second rod
mass1 = plot(x1(1), y1(1), 'bo', 'MarkerFaceColor', 'b'); % Mass 1
mass2 = plot(x2(1), y2(1), 'ro', 'MarkerFaceColor', 'r'); % Mass 2

% Title and labels
title('Double Pendulum Motion');
xlabel('X position (m)');
ylabel('Y position (m)');

% Animation loop
for i = 1:length(time)
    % Update the positions of the rods and masses
    rod1.XData = [0, x1(i)];
    rod1.YData = [0, y1(i)];
    rod2.XData = [x1(i), x2(i)];
    rod2.YData = [y1(i), y2(i)];
    mass1.XData = x1(i);
    mass1.YData = y1(i);
    mass2.XData = x2(i);
    mass2.YData = y2(i);
    
    % Pause to slow down the animation
    pause(0.01);

end

% Plot the results (angles and angular velocities)
figure;
subplot(2, 1, 1);
plot(time, theta1, 'r', 'LineWidth', 1.5);
hold on;
plot(time, theta2, 'b', 'LineWidth', 1.5);
title('Pendulum Angles vs Time');
xlabel('Time (s)');
ylabel('Angle (rad)');
legend('Theta 1', 'Theta 2');

subplot(2, 1, 2);
plot(time, sol(:, 2), 'r', 'LineWidth', 1.5); % Angular velocity of pendulum 1
hold on;
plot(time, sol(:, 4), 'b', 'LineWidth', 1.5); % Angular velocity of pendulum 2
title('Pendulum Angular Velocities vs Time');
xlabel('Time (s)');
ylabel('Angular Velocity (rad/s)');
legend('Theta dot 1', 'Theta dot 2');

% Optional: Save the final figure as a PNG image
% saveas(gcf, 'double_pendulum_simulation.png');
