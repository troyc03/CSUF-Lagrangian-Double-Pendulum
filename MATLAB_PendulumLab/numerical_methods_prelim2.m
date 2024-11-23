% PRELIMINARY: Numerical Integration/Differentiation

% Now that you are familiar with numerical differentiation, 
% we can begin learning about the concepts of numerical integration. 
% Let's begin with Trapezoidal and Simpson's Rules, one of the most
% fundamental concepts of calculus. 

% NUMERICAL INTEGRATION PART 1: Integration by Trapezoidal Rule

% Consider the following example:

f = @(x) x^2 + 3*x + 4;
a = 1;
b = 1.5;
M = 4;

disp('Evaluated integral of f(x) using Trapezoidal Rule:');
s = traprl(f, a, b, M);
disp(s);

function s = traprl(f, a, b, M)
    h = (b - a) / M;
    s = 0;
    for k = 1:(M - 1)
        x = a + h * k;
        s = s + feval(f, x);
    end
    s = h * (feval(f, a) + feval(f, b)) / 2 + h * s;
end

% NUMERICAL INTEGRATION PART 2: Numerical integration by Simpson's Rule

% Consider the following example

f = @(x) x^4 + 3*x^3 + 2*x^2 + x + 1;
a = 2;
b = 3;
M = 2; 

disp('Evaluated integral of f(x) using Simpson''s Rule:');
s = simprl(f, a, b, M);
disp(s);

function s = simprl(f, a, b, M)
    h = (b - a) / (2 * M);  
    s1 = 0;  
    s2 = 0;  
    for k = 1:M
        x = a + h * (2 * k - 1);  
        s1 = s1 + feval(f, x);
    end
    
    for k = 1:M-1
        x = a + h * 2 * k;  
        s2 = s2 + feval(f, x);
    end
    
    s = (h / 3) * (feval(f, a) + feval(f, b) + 4 * s1 + 2 * s2);
end
