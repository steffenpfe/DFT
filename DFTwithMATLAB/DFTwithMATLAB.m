%DFT of a sine wave with noise

%sample rate
dT = 0.1;
%window length
T = 100;
%amaount of samples
N = T/dT;
%time axis
t = [0:dT:T-dT];
%frequency axis
f = [0:1/T:1/dT - 1/T];
%sine wave
s = sin(2*pi*1*t);
%noise
ns = (rand(1,N)-0.5)*2; %-1 - 1
%signal with noise
sr = s + ns;
%DFT
yf_s = fft(s);
yf_sr = fft(sr);
%plots
figure(1)
subplot(2,1,1)
plot(t, sr)
subplot(2,1,2)
plot(f, abs(yf_sr))
figure(2)
plot(t,s)
