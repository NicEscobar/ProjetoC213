a1 = 0.9956;
b1 = 0.003743;

Kp = 5;
Ki = 8;
Kd = 10.25;

Ts = 0.1;

SP = 1;
PV = 0;

resp_6 = 0;
AcaoIntegral = 0;
ErroAnterior = SP - PV;

tempo = 0:0.1:6;

for i = 0.1:0.1:6
  Erro = SP - PV;
  
  AcaoProporcional = Kp*Erro;
  AcaoIntegral = AcaoIntegral + Ki*Ts*Erro;
  AcaoDerivativa = ((Erro - ErroAnterior)/Ts)*Kd;
  
  ErroAnterior  = Erro;
  
  AcaoControlador = AcaoProporcional + AcaoIntegral + AcaoDerivativa;
  
  PV = a1*PV + b1*AcaoControlador;
  resp_6 = [resp_6 PV];
 
end

plot(tempo,resp_6)
plot.show()