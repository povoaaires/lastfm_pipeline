# Last Pipeline
<html>

<div class="introduction">
<p>
Extração de dados do site Last.fm via API 
</p>
</div>

<br>
<div class="tech">
<h2>Tecnologias</h2><br>


<table>

<tr>
<td width="30%">
        <img src="https://github.com/povoaaires/lastfm_pipeline/blob/main/assets/ADLS.png"style="width=125; height:75px;">
    </td>
    <td style="width:100">Separado em três camadas, raw, cleansed e curated, sendo que a primeira camada recebe o dado cru, a intermediária faz a agregação de todos os dados em um único arquivo e a camada curated é a de disponibilização para o cliente final consumir
    </td>

</tr>

<tr>
<td width="30%">
        <img src="https://github.com/povoaaires/lastfm_pipeline/blob/main/assets/python.png"style="width=125; height:75px;">
    </td>
    <td style="width:100">Linguagem de programação utilizada para realizar a extração desses dados do site bem como fazer as devidas tratativas.
    </td>

</tr>


</table>

</div>

<br><br>
<div class="flow">
<h2>Arquitetura</h2><br>

<img src="https://github.com/povoaaires/lastfm_pipeline/blob/main/assets/arch_flow.png">

</div>

</html>