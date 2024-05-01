clc
clear all
close all
a= [1,2,3]
b= [4,5,6]
Sum = 0
for i = 1:length(a)
    Sum=Sum+(a(i) * b(i))
end
disp(['dot product of two lists : ', num2str(sum)])
