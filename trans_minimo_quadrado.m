[L, C] = size(resp0_2);

if (L > 1)
  F = [resp0_2(1:L-1,1) degrau0_2(1:L-1,1)];
  J = [resp0_2(2:L,1)];
elseif (C > 1)
  F = [resp0_2(1,1:C-1); degrau0_2(1,1:C-1)]';
  J = [resp0_2(1,2:C)]';
end

Theta = inv(F'*F)*F'*J;

a1 = Theta(1)
b1 = Theta(2)

sysZ = tf(b1,[1 -a1],0.2) %Tempo de amostragem de 0.1 segundos
sysS = d2c(sysZ)

respmq = 50*step(sysS, tempo0_2)  

plot(tempo0_2, respmq)

