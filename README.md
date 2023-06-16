# Parte prática da prova 2 

## Explicação

Para o desenvolvimento do código e identificação dos rostos foi feito o arquivo 'main.py' que está dentro da pasta atividade. O método utilizado foi o haar cascade. Primeiramente, utilizei um filtro em cada frame para deixá-lo cinza e depois utilizei o próprio haar cascade para detectar as faces.
Depois que a detecção foi feita, utilizamos os pontos da primeira face encontrada 'faces[0]' que foram salvos em x,y,w,h, utilizamos o '.rectangle' do cv2 para fazer o desenho dos retângulos nos frames utilizando os pontos encontrados anteriormente.

Por fim salvamos o resultado no output_video, o vídeo para demonstração está salvo em atividade > saida > out.avi 

Por hoje é só professor :)
