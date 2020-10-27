[L, C] = size(resp0_2);

%Verifico se é um vetor linha ou  coluna
if (L > 1)
  F = [resp0_2(1:L-1,1) degrau0_2(1:L-1,1)];
  J = [resp0_2(2:L,1)];
elseif (C > 1)
  F = [resp0_2(1,1:C-1); degrau0_2(1,1:C-1)]';
  J = [resp0_2(1,2:C)]';
end

%Cálculo matricial
Theta = inv(F'*F)*F'*J;
%Obtendo os parametros a1 e b1
a1 = Theta(1)
b1 = Theta(2)

%Limpando a workspace
clear L
clear C
clear F
clear J
clear Theta

%Resposta das amostras
%plot(tempo0_2, resp0_2);

%Tempo de amostragem de 0.2 segundos
%Função de transferência, domínio Z
sysZ = tf(b1,[1 -a1],0.2)
%Função de transferência, domínio S
sysS = d2c(sysZ)
 
%resposta ao  degrau unitário de alplitude 50
resp_identificada = 50*step(sysS,tempo0_2);

plot(tempo0_2,resp_identificada,tempo0_2,resp0_2);
