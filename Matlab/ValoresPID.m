mp = 0.15;
ts = 75;

dividendo = (((log(mp))/pi)^2);
divisor = (1+((log(mp)) /pi)^2);

%equação do CSI
csi = sqrt(dividendo/divisor)

%equação maximo de pico
wn = 4/(csi*ts);

wcg = wn;

%asind = arco seno angulo em grau
%MF = margem dem fase
MF = 2*asind(csi);

%k(ganho) da função da  malha aberta
k = 80;
%tal da função em malha aberta
tal = 16;

G=(k/((tal*wcg*i)+1));
modG = abs(G);
faseG = angle(G)*180/pi;
%modulo do controlador
modC = 1/modG;
%fase do controlador
faseC = -180+MF-faseG;

kp = (sqrt((modC^2)/(1+(tand(faseC))*((-1)^2))))
ki = (tand(faseC)*(-1)*wcg*kp)
kd = 0





