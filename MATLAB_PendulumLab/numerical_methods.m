% File name: numerical_methods.m
% Author name: Troy Chin
% Version: 1.0
% Purpose: This file will solve for the linear ODEs using the
% implemented numerical methods for this lab.

% Now that you are familiar with numerical integration and differentiation,
% we can finally move onto their applications in solving ODEs using the
% following methods: Euler, Runge-Kutta and the Midpoint Rule.

h=0.05;
x = 0:h:100;
y = zeros(1,length(x));
y(1) = -0.5;


