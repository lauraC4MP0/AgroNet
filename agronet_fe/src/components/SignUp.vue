<template>
  <div class="main-component">
    <form v-on:submit.prevent="processSignUp">
      <h3>Crear cuenta</h3>
      <br/>
      <input type="text" v-model="user.id" placeholder="Número de documento de identidad" required />
      <br />
      <input type="text" v-model="user.usersname" placeholder="username" required />
      <br />
      <input type="text" v-model="user.name_user" placeholder="Nombres" required />
      <br />
      <input type="text" v-model="user.lastname_user" placeholder="Apellidos" required />
      <br />
      <input type="tel" v-model="user.num_phone" placeholder="Teléfono" required />
      <br />
      <input type="email" v-model="user.email" placeholder="Correo electrónico" required />
      <br />
      <input type="password" v-model="user.password" placeholder="Contraseña (8 carácteres)" minlength="8" required />
      <br />
      <input type="password" placeholder="Confirma tu contraseña" minlength="8" required />
      <br />
      <input type="text" v-model="user.address_user" placeholder="Dirección" required />
      <br />
      <select v-model="user.sex_user">
        <option>Sexo</option>
        <option value="Masculino">Masculino</option>
        <option value="Femenino">Femenino</option>
        <option>No binario</option>
        <option>Otro</option>
      </select>
      <br />
   
     
      <select v-model="user.id_city">
        <option value="1" >MEDELLIN</option>
<option value="2" >ABEJORRAL</option>
<option value="3" >ABRIAQUI</option>
<option value="4" >ALEJANDRIA</option>
<option value="5" >AMAGA</option>
<option value="6" >AMALFI</option>
<option value="7" >ANDES</option>
<option value="8" >ANGELOPOLIS</option>
<option value="9" >ANGOSTURA</option>
<option value="10" >ANORI</option>
<option value="11" >SANTAFE DE ANTIOQUIA</option>
<option value="12" >ANZA</option>
<option value="13" >APARTADO</option>
<option value="14" >ARBOLETES</option>
<option value="15" >ARGELIA</option>
<option value="16" >ARMENIA</option>
<option value="17" >BARBOSA</option>
<option value="18" >BELMIRA</option>
<option value="19" >BELLO</option>
<option value="20" >BETANIA</option>
<option value="21" >BETULIA</option>
<option value="22" >CIUDAD BOLIVAR</option>
<option value="23" >BRICEÑO</option>
<option value="24" >BURITICA</option>
<option value="25" >CACERES</option>
<option value="26" >CAICEDO</option>
<option value="27" >CALDAS</option>
<option value="28" >CAMPAMENTO</option>
<option value="29" >CAÑASGORDAS</option>
<option value="30" >CARACOLI</option>
<option value="31" >CARAMANTA</option>
<option value="32" >CAREPA</option>
<option value="33" >EL CARMEN DE VIBORAL</option>
<option value="34" >CAROLINA</option>
<option value="35" >CAUCASIA</option>
<option value="36" >CHIGORODO</option>
<option value="37" >CISNEROS</option>
<option value="38" >COCORNA</option>
<option value="39" >CONCEPCION</option>
<option value="40" >CONCORDIA</option>
<option value="41" >COPACABANA</option>
<option value="42" >DABEIBA</option>
<option value="43" >DON MATIAS</option>
<option value="44" >EBEJICO</option>
<option value="45" >EL BAGRE</option>
<option value="46" >ENTRERRIOS</option>
<option value="47" >ENVIGADO</option>
<option value="48" >FREDONIA</option>
<option value="49" >FRONTINO</option>
<option value="50" >GIRALDO</option>
<option value="51" >GIRARDOTA</option>
<option value="52" >GOMEZ PLATA</option>
<option value="53" >GRANADA</option>
<option value="54" >GUADALUPE</option>
<option value="55" >GUARNE</option>
<option value="56" >GUATAPE</option>
<option value="57" >HELICONIA</option>
<option value="58" >HISPANIA</option>
<option value="59" >ITAGUI</option>
<option value="60" >ITUANGO</option>
<option value="61" >JARDIN</option>
<option value="62" >JERICO</option>
<option value="63" >LA CEJA</option>
<option value="64" >LA ESTRELLA</option>
<option value="65" >LA PINTADA</option>
<option value="66" >LA UNION</option>
<option value="67" >LIBORINA</option>
<option value="68" >MACEO</option>
<option value="69" >MARINILLA</option>
<option value="70" >MONTEBELLO</option>
<option value="71" >MURINDO</option>
<option value="72" >MUTATA</option>
<option value="73" >NARIÑO</option>
<option value="74" >NECOCLI</option>
<option value="75" >NECHI</option>
<option value="76" >OLAYA</option>
<option value="77" >PEÐOL</option>
<option value="78" >PEQUE</option>
<option value="79" >PUEBLORRICO</option>
<option value="80" >PUERTO BERRIO</option>
<option value="81" >PUERTO NARE</option>
<option value="82" >PUERTO TRIUNFO</option>
<option value="83" >REMEDIOS</option>
<option value="84" >RETIRO</option>
<option value="85" >RIONEGRO</option>
<option value="86" >SABANALARGA</option>
<option value="87" >SABANETA</option>
<option value="88" >SALGAR</option>
<option value="89" >SAN ANDRES DE CUERQUIA</option>
<option value="90" >SAN CARLOS</option>
<option value="91" >SAN FRANCISCO</option>
<option value="92" >SAN JERONIMO</option>
<option value="93" >SAN JOSE DE LA MONTAÑA</option>
<option value="94" >SAN JUAN DE URABA</option>
<option value="95" >SAN LUIS</option>
<option value="96" >SAN PEDRO</option>
<option value="97" >SAN PEDRO DE URABA</option>
<option value="98" >SAN RAFAEL</option>
<option value="99" >SAN ROQUE</option>
<option value="100" >SAN VICENTE</option>
<option value="101" >SANTA BARBARA</option>
<option value="102" >SANTA ROSA DE OSOS</option>
<option value="103" >SANTO DOMINGO</option>
<option value="104" >EL SANTUARIO</option>
<option value="105" >SEGOVIA</option>
<option value="106" >SONSON</option>
<option value="107" >SOPETRAN</option>
<option value="108" >TAMESIS</option>
<option value="109" >TARAZA</option>
<option value="110" >TARSO</option>
<option value="111" >TITIRIBI</option>
<option value="112" >TOLEDO</option>
<option value="113" >TURBO</option>
<option value="114" >URAMITA</option>
<option value="115" >URRAO</option>
<option value="116" >VALDIVIA</option>
<option value="117" >VALPARAISO</option>
<option value="118" >VEGACHI</option>
<option value="119" >VENECIA</option>
<option value="120" >VIGIA DEL FUERTE</option>
<option value="121" >YALI</option>
<option value="122" >YARUMAL</option>
<option value="123" >YOLOMBO</option>
<option value="124" >YONDO</option>
<option value="125" >ZARAGOZA</option>
<option value="126" >BARRANQUILLA</option>
<option value="127" >BARANOA</option>
<option value="128" >CAMPO DE LA CRUZ</option>
<option value="129" >CANDELARIA</option>
<option value="130" >GALAPA</option>
<option value="131" >JUAN DE ACOSTA</option>
<option value="132" >LURUACO</option>
<option value="133" >MALAMBO</option>
<option value="134" >MANATI</option>
<option value="135" >PALMAR DE VARELA</option>
<option value="136" >PIOJO</option>
<option value="137" >POLONUEVO</option>
<option value="138" >PONEDERA</option>
<option value="139" >PUERTO COLOMBIA</option>
<option value="140" >REPELON</option>
<option value="141" >SABANAGRANDE</option>
<option value="142" >SABANALARGA</option>
<option value="143" >SANTA LUCIA</option>
<option value="144" >SANTO TOMAS</option>
<option value="145" >SOLEDAD</option>
<option value="146" >SUAN</option>
<option value="147" >TUBARA</option>
<option value="148" >USIACURI</option>
<option value="149" >BOGOTA, D.C.</option>
<option value="150" >CARTAGENA</option>
<option value="151" >ACHI</option>
<option value="152" >ALTOS DEL ROSARIO</option>
<option value="153" >ARENAL</option>
<option value="154" >ARJONA</option>
<option value="155" >ARROYOHONDO</option>
<option value="156" >BARRANCO DE LOBA</option>
<option value="157" >CALAMAR</option>
<option value="158" >CANTAGALLO</option>
<option value="159" >CICUCO</option>
<option value="160" >CORDOBA</option>
<option value="161" >CLEMENCIA</option>
<option value="162" >EL CARMEN DE BOLIVAR</option>
<option value="163" >EL GUAMO</option>
<option value="164" >EL PEÑON</option>
<option value="165" >HATILLO DE LOBA</option>
<option value="166" >MAGANGUE</option>
<option value="167" >MAHATES</option>
<option value="168" >MARGARITA</option>
<option value="169" >MARIA LA BAJA</option>
<option value="170" >MONTECRISTO</option>
<option value="171" >MOMPOS</option>
<option value="172" >NOROSI</option>
<option value="173" >MORALES</option>
<option value="174" >PINILLOS</option>
<option value="175" >REGIDOR</option>
<option value="176" >RIO VIEJO</option>
<option value="177" >SAN CRISTOBAL</option>
<option value="178" >SAN ESTANISLAO</option>
<option value="179" >SAN FERNANDO</option>
<option value="180" >SAN JACINTO</option>
<option value="181" >SAN JACINTO DEL CAUCA</option>
<option value="182" >SAN JUAN NEPOMUCENO</option>
<option value="183" >SAN MARTIN DE LOBA</option>
<option value="184" >SAN PABLO</option>
<option value="185" >SANTA CATALINA</option>
<option value="186" >SANTA ROSA</option>
<option value="187" >SANTA ROSA DEL SUR</option>
<option value="188" >SIMITI</option>
<option value="189" >SOPLAVIENTO</option>
<option value="190" >TALAIGUA NUEVO</option>
<option value="191" >TIQUISIO</option>
<option value="192" >TURBACO</option>
<option value="193" >TURBANA</option>
<option value="194" >VILLANUEVA</option>
<option value="195" >ZAMBRANO</option>
<option value="196" >TUNJA</option>
<option value="197" >ALMEIDA</option>
<option value="198" >AQUITANIA</option>
<option value="199" >ARCABUCO</option>
<option value="200" >BELEN</option>
<option value="201" >BERBEO</option>
<option value="202" >BETEITIVA</option>
<option value="203" >BOAVITA</option>
<option value="204" >BOYACA</option>
<option value="205" >BRICEÑO</option>
<option value="206" >BUENAVISTA</option>
<option value="207" >BUSBANZA</option>
<option value="208" >CALDAS</option>
<option value="209" >CAMPOHERMOSO</option>
<option value="210" >CERINZA</option>
<option value="211" >CHINAVITA</option>
<option value="212" >CHIQUINQUIRA</option>
<option value="213" >CHISCAS</option>
<option value="214" >CHITA</option>
<option value="215" >CHITARAQUE</option>
<option value="216" >CHIVATA</option>
<option value="217" >CIENEGA</option>
<option value="218" >COMBITA</option>
<option value="219" >COPER</option>
<option value="220" >CORRALES</option>
<option value="221" >COVARACHIA</option>
<option value="222" >CUBARA</option>
<option value="223" >CUCAITA</option>
<option value="224" >CUITIVA</option>
<option value="225" >CHIQUIZA</option>
<option value="226" >CHIVOR</option>
<option value="227" >DUITAMA</option>
<option value="228" >EL COCUY</option>
<option value="229" >EL ESPINO</option>
<option value="230" >FIRAVITOBA</option>
<option value="231" >FLORESTA</option>
<option value="232" >GACHANTIVA</option>
<option value="233" >GAMEZA</option>
<option value="234" >GARAGOA</option>
<option value="235" >GUACAMAYAS</option>
<option value="236" >GUATEQUE</option>
<option value="237" >GUAYATA</option>
<option value="238" >GsICAN</option>
<option value="239" >IZA</option>
<option value="240" >JENESANO</option>
<option value="241" >JERICO</option>
<option value="242" >LABRANZAGRANDE</option>
<option value="243" >LA CAPILLA</option>
<option value="244" >LA VICTORIA</option>
<option value="245" >LA UVITA</option>
<option value="246" >VILLA DE LEYVA</option>
<option value="247" >MACANAL</option>
<option value="248" >MARIPI</option>
<option value="249" >MIRAFLORES</option>
<option value="250" >MONGUA</option>
<option value="251" >MONGUI</option>
<option value="252" >MONIQUIRA</option>
<option value="253" >MOTAVITA</option>
<option value="254" >MUZO</option>
<option value="255" >NOBSA</option>
<option value="256" >NUEVO COLON</option>
<option value="257" >OICATA</option>
<option value="258" >OTANCHE</option>
<option value="259" >PACHAVITA</option>
<option value="260" >PAEZ</option>
<option value="261" >PAIPA</option>
<option value="262" >PAJARITO</option>
<option value="263" >PANQUEBA</option>
<option value="264" >PAUNA</option>
<option value="265" >PAYA</option>
<option value="266" >PAZ DE RIO</option>
<option value="267" >PESCA</option>
<option value="268" >PISBA</option>
<option value="269" >PUERTO BOYACA</option>
<option value="270" >QUIPAMA</option>
<option value="271" >RAMIRIQUI</option>
<option value="272" >RAQUIRA</option>
<option value="273" >RONDON</option>
<option value="274" >SABOYA</option>
<option value="275" >SACHICA</option>
<option value="276" >SAMACA</option>
<option value="277" >SAN EDUARDO</option>
<option value="278" >SAN JOSE DE PARE</option>
<option value="279" >SAN LUIS DE GACENO</option>
<option value="280" >SAN MATEO</option>
<option value="281" >SAN MIGUEL DE SEMA</option>
<option value="282" >SAN PABLO DE BORBUR</option>
<option value="283" >SANTANA</option>
<option value="284" >SANTA MARIA</option>
<option value="285" >SANTA ROSA DE VITERBO</option>
<option value="286" >SANTA SOFIA</option>
<option value="287" >SATIVANORTE</option>
<option value="288" >SATIVASUR</option>
<option value="289" >SIACHOQUE</option>
<option value="290" >SOATA</option>
<option value="291" >SOCOTA</option>
<option value="292" >SOCHA</option>
<option value="293" >SOGAMOSO</option>
<option value="294" >SOMONDOCO</option>
<option value="295" >SORA</option>
<option value="296" >SOTAQUIRA</option>
<option value="297" >SORACA</option>
<option value="298" >SUSACON</option>
<option value="299" >SUTAMARCHAN</option>
<option value="300" >SUTATENZA</option>
<option value="301" >TASCO</option>
<option value="302" >TENZA</option>
<option value="303" >TIBANA</option>
<option value="304" >TIBASOSA</option>
<option value="305" >TINJACA</option>
<option value="306" >TIPACOQUE</option>
<option value="307" >TOCA</option>
<option value="308" >TOGsI</option>
<option value="309" >TOPAGA</option>
<option value="310" >TOTA</option>
<option value="311" >TUNUNGUA</option>
<option value="312" >TURMEQUE</option>
<option value="313" >TUTA</option>
<option value="314" >TUTAZA</option>
<option value="315" >UMBITA</option>
<option value="316" >VENTAQUEMADA</option>
<option value="317" >VIRACACHA</option>
<option value="318" >ZETAQUIRA</option>
<option value="319" >MANIZALES</option>
<option value="320" >AGUADAS</option>
<option value="321" >ANSERMA</option>
<option value="322" >ARANZAZU</option>
<option value="323" >BELALCAZAR</option>
<option value="324" >CHINCHINA</option>
<option value="325" >FILADELFIA</option>
<option value="326" >LA DORADA</option>
<option value="327" >LA MERCED</option>
<option value="328" >MANZANARES</option>
<option value="329" >MARMATO</option>
<option value="330" >MARQUETALIA</option>
<option value="331" >MARULANDA</option>
<option value="332" >NEIRA</option>
<option value="333" >NORCASIA</option>
<option value="334" >PACORA</option>
<option value="335" >PALESTINA</option>
<option value="336" >PENSILVANIA</option>
<option value="337" >RIOSUCIO</option>
<option value="338" >RISARALDA</option>
<option value="339" >SALAMINA</option>
<option value="340" >SAMANA</option>
<option value="341" >SAN JOSE</option>
<option value="342" >SUPIA</option>
<option value="343" >VICTORIA</option>
<option value="344" >VILLAMARIA</option>
<option value="345" >VITERBO</option>
<option value="346" >FLORENCIA</option>
<option value="347" >ALBANIA</option>
<option value="348" >BELEN DE LOS ANDAQUIES</option>
<option value="349" >CARTAGENA DEL CHAIRA</option>
<option value="350" >CURILLO</option>
<option value="351" >EL DONCELLO</option>
<option value="352" >EL PAUJIL</option>
<option value="353" >LA MONTAÑITA</option>
<option value="354" >MILAN</option>
<option value="355" >MORELIA</option>
<option value="356" >PUERTO RICO</option>
<option value="357" >SAN JOSE DEL FRAGUA</option>
<option value="358" >SAN VICENTE DEL CAGUAN</option>
<option value="359" >SOLANO</option>
<option value="360" >SOLITA</option>
<option value="361" >VALPARAISO</option>
<option value="362" >POPAYAN</option>
<option value="363" >ALMAGUER</option>
<option value="364" >ARGELIA</option>
<option value="365" >BALBOA</option>
<option value="366" >BOLIVAR</option>
<option value="367" >BUENOS AIRES</option>
<option value="368" >CAJIBIO</option>
<option value="369" >CALDONO</option>
<option value="370" >CALOTO</option>
<option value="371" >CORINTO</option>
<option value="372" >EL TAMBO</option>
<option value="373" >FLORENCIA</option>
<option value="374" >GUACHENE</option>
<option value="375" >GUAPI</option>
<option value="376" >INZA</option>
<option value="377" >JAMBALO</option>
<option value="378" >LA SIERRA</option>
<option value="379" >LA VEGA</option>
<option value="380" >LOPEZ</option>
<option value="381" >MERCADERES</option>
<option value="382" >MIRANDA</option>
<option value="383" >MORALES</option>
<option value="384" >PADILLA</option>
<option value="385" >PAEZ</option>
<option value="386" >PATIA</option>
<option value="387" >PIAMONTE</option>
<option value="388" >PIENDAMO</option>
<option value="389" >PUERTO TEJADA</option>
<option value="390" >PURACE</option>
<option value="391" >ROSAS</option>
<option value="392" >SAN SEBASTIAN</option>
<option value="393" >SANTANDER DE QUILICHAO</option>
<option value="394" >SANTA ROSA</option>
<option value="395" >SILVIA</option>
<option value="396" >SOTARA</option>
<option value="397" >SUAREZ</option>
<option value="398" >SUCRE</option>
<option value="399" >TIMBIO</option>
<option value="400" >TIMBIQUI</option>
<option value="401" >TORIBIO</option>
<option value="402" >TOTORO</option>
<option value="403" >VILLA RICA</option>
<option value="404" >VALLEDUPAR</option>
<option value="405" >AGUACHICA</option>
<option value="406" >AGUSTIN CODAZZI</option>
<option value="407" >ASTREA</option>
<option value="408" >BECERRIL</option>
<option value="409" >BOSCONIA</option>
<option value="410" >CHIMICHAGUA</option>
<option value="411" >CHIRIGUANA</option>
<option value="412" >CURUMANI</option>
<option value="413" >EL COPEY</option>
<option value="414" >EL PASO</option>
<option value="415" >GAMARRA</option>
<option value="416" >GONZALEZ</option>
<option value="417" >LA GLORIA</option>
<option value="418" >LA JAGUA DE IBIRICO</option>
<option value="419" >MANAURE</option>
<option value="420" >PAILITAS</option>
<option value="421" >PELAYA</option>
<option value="422" >PUEBLO BELLO</option>
<option value="423" >RIO DE ORO</option>
<option value="424" >LA PAZ</option>
<option value="425" >SAN ALBERTO</option>
<option value="426" >SAN DIEGO</option>
<option value="427" >SAN MARTIN</option>
<option value="428" >TAMALAMEQUE</option>
<option value="429" >MONTERIA</option>
<option value="430" >AYAPEL</option>
<option value="431" >BUENAVISTA</option>
<option value="432" >CANALETE</option>
<option value="433" >CERETE</option>
<option value="434" >CHIMA</option>
<option value="435" >CHINU</option>
<option value="436" >CIENAGA DE ORO</option>
<option value="437" >COTORRA</option>
<option value="438" >LA APARTADA</option>
<option value="439" >LORICA</option>
<option value="440" >LOS CORDOBAS</option>
<option value="441" >MOMIL</option>
<option value="442" >MONTELIBANO</option>
<option value="443" >MOÑITOS</option>
<option value="444" >PLANETA RICA</option>
<option value="445" >PUEBLO NUEVO</option>
<option value="446" >PUERTO ESCONDIDO</option>
<option value="447" >PUERTO LIBERTADOR</option>
<option value="448" >PURISIMA</option>
<option value="449" >SAHAGUN</option>
<option value="450" >SAN ANDRES SOTAVENTO</option>
<option value="451" >SAN ANTERO</option>
<option value="452" >SAN BERNARDO DEL VIENTO</option>
<option value="453" >SAN CARLOS</option>
<option value="454" >SAN PELAYO</option>
<option value="455" >TIERRALTA</option>
<option value="456" >VALENCIA</option>
<option value="457" >AGUA DE DIOS</option>
<option value="458" >ALBAN</option>
<option value="459" >ANAPOIMA</option>
<option value="460" >ANOLAIMA</option>
<option value="461" >ARBELAEZ</option>
<option value="462" >BELTRAN</option>
<option value="463" >BITUIMA</option>
<option value="464" >BOJACA</option>
<option value="465" >CABRERA</option>
<option value="466" >CACHIPAY</option>
<option value="467" >CAJICA</option>
<option value="468" >CAPARRAPI</option>
<option value="469" >CAQUEZA</option>
<option value="470" >CARMEN DE CARUPA</option>
<option value="471" >CHAGUANI</option>
<option value="472" >CHIA</option>
<option value="473" >CHIPAQUE</option>
<option value="474" >CHOACHI</option>
<option value="475" >CHOCONTA</option>
<option value="476" >COGUA</option>
<option value="477" >COTA</option>
<option value="478" >CUCUNUBA</option>
<option value="479" >EL COLEGIO</option>
<option value="480" >EL PEÑON</option>
<option value="481" >EL ROSAL</option>
<option value="482" >FACATATIVA</option>
<option value="483" >FOMEQUE</option>
<option value="484" >FOSCA</option>
<option value="485" >FUNZA</option>
<option value="486" >FUQUENE</option>
<option value="487" >FUSAGASUGA</option>
<option value="488" >GACHALA</option>
<option value="489" >GACHANCIPA</option>
<option value="490" >GACHETA</option>
<option value="491" >GAMA</option>
<option value="492" >GIRARDOT</option>
<option value="493" >GRANADA</option>
<option value="494" >GUACHETA</option>
<option value="495" >GUADUAS</option>
<option value="496" >GUASCA</option>
<option value="497" >GUATAQUI</option>
<option value="498" >GUATAVITA</option>
<option value="499" >GUAYABAL DE SIQUIMA</option>
<option value="500" >GUAYABETAL</option>
<option value="501" >GUTIERREZ</option>
<option value="502" >JERUSALEN</option>
<option value="503" >JUNIN</option>
<option value="504" >LA CALERA</option>
<option value="505" >LA MESA</option>
<option value="506" >LA PALMA</option>
<option value="507" >LA PEÑA</option>
<option value="508" >LA VEGA</option>
<option value="509" >LENGUAZAQUE</option>
<option value="510" >MACHETA</option>
<option value="511" >MADRID</option>
<option value="512" >MANTA</option>
<option value="513" >MEDINA</option>
<option value="514" >MOSQUERA</option>
<option value="515" >NARIÑO</option>
<option value="516" >NEMOCON</option>
<option value="517" >NILO</option>
<option value="518" >NIMAIMA</option>
<option value="519" >NOCAIMA</option>
<option value="520" >VENECIA</option>
<option value="521" >PACHO</option>
<option value="522" >PAIME</option>
<option value="523" >PANDI</option>
<option value="524" >PARATEBUENO</option>
<option value="525" >PASCA</option>
<option value="526" >PUERTO SALGAR</option>
<option value="527" >PULI</option>
<option value="528" >QUEBRADANEGRA</option>
<option value="529" >QUETAME</option>
<option value="530" >QUIPILE</option>
<option value="531" >APULO</option>
<option value="532" >RICAURTE</option>
<option value="533" >SAN ANTONIO DEL TEQUENDAMA</option>
<option value="534" >SAN BERNARDO</option>
<option value="535" >SAN CAYETANO</option>
<option value="536" >SAN FRANCISCO</option>
<option value="537" >SAN JUAN DE RIO SECO</option>
<option value="538" >SASAIMA</option>
<option value="539" >SESQUILE</option>
<option value="540" >SIBATE</option>
<option value="541" >SILVANIA</option>
<option value="542" >SIMIJACA</option>
<option value="543" >SOACHA</option>
<option value="544" >SOPO</option>
<option value="545" >SUBACHOQUE</option>
<option value="546" >SUESCA</option>
<option value="547" >SUPATA</option>
<option value="548" >SUSA</option>
<option value="549" >SUTATAUSA</option>
<option value="550" >TABIO</option>
<option value="551" >TAUSA</option>
<option value="552" >TENA</option>
<option value="553" >TENJO</option>
<option value="554" >TIBACUY</option>
<option value="555" >TIBIRITA</option>
<option value="556" >TOCAIMA</option>
<option value="557" >TOCANCIPA</option>
<option value="558" >TOPAIPI</option>
<option value="559" >UBALA</option>
<option value="560" >UBAQUE</option>
<option value="561" >VILLA DE SAN DIEGO DE UBATE</option>
<option value="562" >UNE</option>
<option value="563" >UTICA</option>
<option value="564" >VERGARA</option>
<option value="565" >VIANI</option>
<option value="566" >VILLAGOMEZ</option>
<option value="567" >VILLAPINZON</option>
<option value="568" >VILLETA</option>
<option value="569" >VIOTA</option>
<option value="570" >YACOPI</option>
<option value="571" >ZIPACON</option>
<option value="572" >ZIPAQUIRA</option>
<option value="573" >QUIBDO</option>
<option value="574" >ACANDI</option>
<option value="575" >ALTO BAUDO</option>
<option value="576" >ATRATO</option>
<option value="577" >BAGADO</option>
<option value="578" >BAHIA SOLANO</option>
<option value="579" >BAJO BAUDO</option>
<option value="580" >BOJAYA</option>
<option value="581" >EL CANTON DEL SAN PABLO</option>
<option value="582" >CARMEN DEL DARIEN</option>
<option value="583" >CERTEGUI</option>
<option value="584" >CONDOTO</option>
<option value="585" >EL CARMEN DE ATRATO</option>
<option value="586" >EL LITORAL DEL SAN JUAN</option>
<option value="587" >ISTMINA</option>
<option value="588" >JURADO</option>
<option value="589" >LLORO</option>
<option value="590" >MEDIO ATRATO</option>
<option value="591" >MEDIO BAUDO</option>
<option value="592" >MEDIO SAN JUAN</option>
<option value="593" >NOVITA</option>
<option value="594" >NUQUI</option>
<option value="595" >RIO IRO</option>
<option value="596" >RIO QUITO</option>
<option value="597" >RIOSUCIO</option>
<option value="598" >SAN JOSE DEL PALMAR</option>
<option value="599" >SIPI</option>
<option value="600" >TADO</option>
<option value="601" >UNGUIA</option>
<option value="602" >UNION PANAMERICANA</option>
<option value="603" >NEIVA</option>
<option value="604" >ACEVEDO</option>
<option value="605" >AGRADO</option>
<option value="606" >AIPE</option>
<option value="607" >ALGECIRAS</option>
<option value="608" >ALTAMIRA</option>
<option value="609" >BARAYA</option>
<option value="610" >CAMPOALEGRE</option>
<option value="611" >COLOMBIA</option>
<option value="612" >ELIAS</option>
<option value="613" >GARZON</option>
<option value="614" >GIGANTE</option>
<option value="615" >GUADALUPE</option>
<option value="616" >HOBO</option>
<option value="617" >IQUIRA</option>
<option value="618" >ISNOS</option>
<option value="619" >LA ARGENTINA</option>
<option value="620" >LA PLATA</option>
<option value="621" >NATAGA</option>
<option value="622" >OPORAPA</option>
<option value="623" >PAICOL</option>
<option value="624" >PALERMO</option>
<option value="625" >PALESTINA</option>
<option value="626" >PITAL</option>
<option value="627" >PITALITO</option>
<option value="628" >RIVERA</option>
<option value="629" >SALADOBLANCO</option>
<option value="630" >SAN AGUSTIN</option>
<option value="631" >SANTA MARIA</option>
<option value="632" >SUAZA</option>
<option value="633" >TARQUI</option>
<option value="634" >TESALIA</option>
<option value="635" >TELLO</option>
<option value="636" >TERUEL</option>
<option value="637" >TIMANA</option>
<option value="638" >VILLAVIEJA</option>
<option value="639" >YAGUARA</option>
<option value="640" >RIOHACHA</option>
<option value="641" >ALBANIA</option>
<option value="642" >BARRANCAS</option>
<option value="643" >DIBULLA</option>
<option value="644" >DISTRACCION</option>
<option value="645" >EL MOLINO</option>
<option value="646" >FONSECA</option>
<option value="647" >HATONUEVO</option>
<option value="648" >LA JAGUA DEL PILAR</option>
<option value="649" >MAICAO</option>
<option value="650" >MANAURE</option>
<option value="651" >SAN JUAN DEL CESAR</option>
<option value="652" >URIBIA</option>
<option value="653" >URUMITA</option>
<option value="654" >VILLANUEVA</option>
<option value="655" >SANTA MARTA</option>
<option value="656" >ALGARROBO</option>
<option value="657" >ARACATACA</option>
<option value="658" >ARIGUANI</option>
<option value="659" >CERRO SAN ANTONIO</option>
<option value="660" >CHIBOLO</option>
<option value="661" >CIENAGA</option>
<option value="662" >CONCORDIA</option>
<option value="663" >EL BANCO</option>
<option value="664" >EL PIÑON</option>
<option value="665" >EL RETEN</option>
<option value="666" >FUNDACION</option>
<option value="667" >GUAMAL</option>
<option value="668" >NUEVA GRANADA</option>
<option value="669" >PEDRAZA</option>
<option value="670" >PIJIÑO DEL CARMEN</option>
<option value="671" >PIVIJAY</option>
<option value="672" >PLATO</option>
<option value="673" >PUEBLOVIEJO</option>
<option value="674" >REMOLINO</option>
<option value="675" >SABANAS DE SAN ANGEL</option>
<option value="676" >SALAMINA</option>
<option value="677" >SAN SEBASTIAN DE BUENAVISTA</option>
<option value="678" >SAN ZENON</option>
<option value="679" >SANTA ANA</option>
<option value="680" >SANTA BARBARA DE PINTO</option>
<option value="681" >SITIONUEVO</option>
<option value="682" >TENERIFE</option>
<option value="683" >ZAPAYAN</option>
<option value="684" >ZONA BANANERA</option>
<option value="685" >VILLAVICENCIO</option>
<option value="686" >ACACIAS</option>
<option value="687" >BARRANCA DE UPIA</option>
<option value="688" >CABUYARO</option>
<option value="689" >CASTILLA LA NUEVA</option>
<option value="690" >CUBARRAL</option>
<option value="691" >CUMARAL</option>
<option value="692" >EL CALVARIO</option>
<option value="693" >EL CASTILLO</option>
<option value="694" >EL DORADO</option>
<option value="695" >FUENTE DE ORO</option>
<option value="696" >GRANADA</option>
<option value="697" >GUAMAL</option>
<option value="698" >MAPIRIPAN</option>
<option value="699" >MESETAS</option>
<option value="700" >LA MACARENA</option>
<option value="701" >URIBE</option>
<option value="702" >LEJANIAS</option>
<option value="703" >PUERTO CONCORDIA</option>
<option value="704" >PUERTO GAITAN</option>
<option value="705" >PUERTO LOPEZ</option>
<option value="706" >PUERTO LLERAS</option>
<option value="707" >PUERTO RICO</option>
<option value="708" >RESTREPO</option>
<option value="709" >SAN CARLOS DE GUAROA</option>
<option value="710" >SAN JUAN DE ARAMA</option>
<option value="711" >SAN JUANITO</option>
<option value="712" >SAN MARTIN</option>
<option value="713" >VISTAHERMOSA</option>
<option value="714" >PASTO</option>
<option value="715" >ALBAN</option>
<option value="716" >ALDANA</option>
<option value="717" >ANCUYA</option>
<option value="718" >ARBOLEDA</option>
<option value="719" >BARBACOAS</option>
<option value="720" >BELEN</option>
<option value="721" >BUESACO</option>
<option value="722" >COLON</option>
<option value="723" >CONSACA</option>
<option value="724" >CONTADERO</option>
<option value="725" >CORDOBA</option>
<option value="726" >CUASPUD</option>
<option value="727" >CUMBAL</option>
<option value="728" >CUMBITARA</option>
<option value="729" >CHACHAGsI</option>
<option value="730" >EL CHARCO</option>
<option value="731" >EL PEÑOL</option>
<option value="732" >EL ROSARIO</option>
<option value="733" >EL TABLON DE GOMEZ</option>
<option value="734" >EL TAMBO</option>
<option value="735" >FUNES</option>
<option value="736" >GUACHUCAL</option>
<option value="737" >GUAITARILLA</option>
<option value="738" >GUALMATAN</option>
<option value="739" >ILES</option>
<option value="740" >IMUES</option>
<option value="741" >IPIALES</option>
<option value="742" >LA CRUZ</option>
<option value="743" >LA FLORIDA</option>
<option value="744" >LA LLANADA</option>
<option value="745" >LA TOLA</option>
<option value="746" >LA UNION</option>
<option value="747" >LEIVA</option>
<option value="748" >LINARES</option>
<option value="749" >LOS ANDES</option>
<option value="750" >MAGsI</option>
<option value="751" >MALLAMA</option>
<option value="752" >MOSQUERA</option>
<option value="753" >NARIÑO</option>
<option value="754" >OLAYA HERRERA</option>
<option value="755" >OSPINA</option>
<option value="756" >FRANCISCO PIZARRO</option>
<option value="757" >POLICARPA</option>
<option value="758" >POTOSI</option>
<option value="759" >PROVIDENCIA</option>
<option value="760" >PUERRES</option>
<option value="761" >PUPIALES</option>
<option value="762" >RICAURTE</option>
<option value="763" >ROBERTO PAYAN</option>
<option value="764" >SAMANIEGO</option>
<option value="765" >SANDONA</option>
<option value="766" >SAN BERNARDO</option>
<option value="767" >SAN LORENZO</option>
<option value="768" >SAN PABLO</option>
<option value="769" >SAN PEDRO DE CARTAGO</option>
<option value="770" >SANTA BARBARA</option>
<option value="771" >SANTACRUZ</option>
<option value="772" >SAPUYES</option>
<option value="773" >TAMINANGO</option>
<option value="774" >TANGUA</option>
<option value="775" >SAN ANDRES DE TUMACO</option>
<option value="776" >TUQUERRES</option>
<option value="777" >YACUANQUER</option>
<option value="778" >CUCUTA</option>
<option value="779" >ABREGO</option>
<option value="780" >ARBOLEDAS</option>
<option value="781" >BOCHALEMA</option>
<option value="782" >BUCARASICA</option>
<option value="783" >CACOTA</option>
<option value="784" >CACHIRA</option>
<option value="785" >CHINACOTA</option>
<option value="786" >CHITAGA</option>
<option value="787" >CONVENCION</option>
<option value="788" >CUCUTILLA</option>
<option value="789" >DURANIA</option>
<option value="790" >EL CARMEN</option>
<option value="791" >EL TARRA</option>
<option value="792" >EL ZULIA</option>
<option value="793" >GRAMALOTE</option>
<option value="794" >HACARI</option>
<option value="795" >HERRAN</option>
<option value="796" >LABATECA</option>
<option value="797" >LA ESPERANZA</option>
<option value="798" >LA PLAYA</option>
<option value="799" >LOS PATIOS</option>
<option value="800" >LOURDES</option>
<option value="801" >MUTISCUA</option>
<option value="802" >OCAÑA</option>
<option value="803" >PAMPLONA</option>
<option value="804" >PAMPLONITA</option>
<option value="805" >PUERTO SANTANDER</option>
<option value="806" >RAGONVALIA</option>
<option value="807" >SALAZAR</option>
<option value="808" >SAN CALIXTO</option>
<option value="809" >SAN CAYETANO</option>
<option value="810" >SANTIAGO</option>
<option value="811" >SARDINATA</option>
<option value="812" >SILOS</option>
<option value="813" >TEORAMA</option>
<option value="814" >TIBU</option>
<option value="815" >TOLEDO</option>
<option value="816" >VILLA CARO</option>
<option value="817" >VILLA DEL ROSARIO</option>
<option value="818" >ARMENIA</option>
<option value="819" >BUENAVISTA</option>
<option value="820" >CALARCA</option>
<option value="821" >CIRCASIA</option>
<option value="822" >CORDOBA</option>
<option value="823" >FILANDIA</option>
<option value="824" >GENOVA</option>
<option value="825" >LA TEBAIDA</option>
<option value="826" >MONTENEGRO</option>
<option value="827" >PIJAO</option>
<option value="828" >QUIMBAYA</option>
<option value="829" >SALENTO</option>
<option value="830" >PEREIRA</option>
<option value="831" >APIA</option>
<option value="832" >BALBOA</option>
<option value="833" >BELEN DE UMBRIA</option>
<option value="834" >DOSQUEBRADAS</option>
<option value="835" >GUATICA</option>
<option value="836" >LA CELIA</option>
<option value="837" >LA VIRGINIA</option>
<option value="838" >MARSELLA</option>
<option value="839" >MISTRATO</option>
<option value="840" >PUEBLO RICO</option>
<option value="841" >QUINCHIA</option>
<option value="842" >SANTA ROSA DE CABAL</option>
<option value="843" >SANTUARIO</option>
<option value="844" >BUCARAMANGA</option>
<option value="845" >AGUADA</option>
<option value="846" >ALBANIA</option>
<option value="847" >ARATOCA</option>
<option value="848" >BARBOSA</option>
<option value="849" >BARICHARA</option>
<option value="850" >BARRANCABERMEJA</option>
<option value="851" >BETULIA</option>
<option value="852" >BOLIVAR</option>
<option value="853" >CABRERA</option>
<option value="854" >CALIFORNIA</option>
<option value="855" >CAPITANEJO</option>
<option value="856" >CARCASI</option>
<option value="857" >CEPITA</option>
<option value="858" >CERRITO</option>
<option value="859" >CHARALA</option>
<option value="860" >CHARTA</option>
<option value="861" >CHIMA</option>
<option value="862" >CHIPATA</option>
<option value="863" >CIMITARRA</option>
<option value="864" >CONCEPCION</option>
<option value="865" >CONFINES</option>
<option value="866" >CONTRATACION</option>
<option value="867" >COROMORO</option>
<option value="868" >CURITI</option>
<option value="869" >EL CARMEN DE CHUCURI</option>
<option value="870" >EL GUACAMAYO</option>
<option value="871" >EL PEÑON</option>
<option value="872" >EL PLAYON</option>
<option value="873" >ENCINO</option>
<option value="874" >ENCISO</option>
<option value="875" >FLORIAN</option>
<option value="876" >FLORIDABLANCA</option>
<option value="877" >GALAN</option>
<option value="878" >GAMBITA</option>
<option value="879" >GIRON</option>
<option value="880" >GUACA</option>
<option value="881" >GUADALUPE</option>
<option value="882" >GUAPOTA</option>
<option value="883" >GUAVATA</option>
<option value="884" >GsEPSA</option>
<option value="885" >HATO</option>
<option value="886" >JESUS MARIA</option>
<option value="887" >JORDAN</option>
<option value="888" >LA BELLEZA</option>
<option value="889" >LANDAZURI</option>
<option value="890" >LA PAZ</option>
<option value="891" >LEBRIJA</option>
<option value="892" >LOS SANTOS</option>
<option value="893" >MACARAVITA</option>
<option value="894" >MALAGA</option>
<option value="895" >MATANZA</option>
<option value="896" >MOGOTES</option>
<option value="897" >MOLAGAVITA</option>
<option value="898" >OCAMONTE</option>
<option value="899" >OIBA</option>
<option value="900" >ONZAGA</option>
<option value="901" >PALMAR</option>
<option value="902" >PALMAS DEL SOCORRO</option>
<option value="903" >PARAMO</option>
<option value="904" >PIEDECUESTA</option>
<option value="905" >PINCHOTE</option>
<option value="906" >PUENTE NACIONAL</option>
<option value="907" >PUERTO PARRA</option>
<option value="908" >PUERTO WILCHES</option>
<option value="909" >RIONEGRO</option>
<option value="910" >SABANA DE TORRES</option>
<option value="911" >SAN ANDRES</option>
<option value="912" >SAN BENITO</option>
<option value="913" >SAN GIL</option>
<option value="914" >SAN JOAQUIN</option>
<option value="915" >SAN JOSE DE MIRANDA</option>
<option value="916" >SAN MIGUEL</option>
<option value="917" >SAN VICENTE DE CHUCURI</option>
<option value="918" >SANTA BARBARA</option>
<option value="919" >SANTA HELENA DEL OPON</option>
<option value="920" >SIMACOTA</option>
<option value="921" >SOCORRO</option>
<option value="922" >SUAITA</option>
<option value="923" >SUCRE</option>
<option value="924" >SURATA</option>
<option value="925" >TONA</option>
<option value="926" >VALLE DE SAN JOSE</option>
<option value="927" >VELEZ</option>
<option value="928" >VETAS</option>
<option value="929" >VILLANUEVA</option>
<option value="930" >ZAPATOCA</option>
<option value="931" >SINCELEJO</option>
<option value="932" >BUENAVISTA</option>
<option value="933" >CAIMITO</option>
<option value="934" >COLOSO</option>
<option value="935" >COROZAL</option>
<option value="936" >COVEÑAS</option>
<option value="937" >CHALAN</option>
<option value="938" >EL ROBLE</option>
<option value="939" >GALERAS</option>
<option value="940" >GUARANDA</option>
<option value="941" >LA UNION</option>
<option value="942" >LOS PALMITOS</option>
<option value="943" >MAJAGUAL</option>
<option value="944" >MORROA</option>
<option value="945" >OVEJAS</option>
<option value="946" >PALMITO</option>
<option value="947" >SAMPUES</option>
<option value="948" >SAN BENITO ABAD</option>
<option value="949" >SAN JUAN DE BETULIA</option>
<option value="950" >SAN MARCOS</option>
<option value="951" >SAN ONOFRE</option>
<option value="952" >SAN PEDRO</option>
<option value="953" >SAN LUIS DE SINCE</option>
<option value="954" >SUCRE</option>
<option value="955" >SANTIAGO DE TOLU</option>
<option value="956" >TOLU VIEJO</option>
<option value="957" >IBAGUE</option>
<option value="958" >ALPUJARRA</option>
<option value="959" >ALVARADO</option>
<option value="960" >AMBALEMA</option>
<option value="961" >ANZOATEGUI</option>
<option value="962" >ARMERO</option>
<option value="963" >ATACO</option>
<option value="964" >CAJAMARCA</option>
<option value="965" >CARMEN DE APICALA</option>
<option value="966" >CASABIANCA</option>
<option value="967" >CHAPARRAL</option>
<option value="968" >COELLO</option>
<option value="969" >COYAIMA</option>
<option value="970" >CUNDAY</option>
<option value="971" >DOLORES</option>
<option value="972" >ESPINAL</option>
<option value="973" >FALAN</option>
<option value="974" >FLANDES</option>
<option value="975" >FRESNO</option>
<option value="976" >GUAMO</option>
<option value="977" >HERVEO</option>
<option value="978" >HONDA</option>
<option value="979" >ICONONZO</option>
<option value="980" >LERIDA</option>
<option value="981" >LIBANO</option>
<option value="982" >MARIQUITA</option>
<option value="983" >MELGAR</option>
<option value="984" >MURILLO</option>
<option value="985" >NATAGAIMA</option>
<option value="986" >ORTEGA</option>
<option value="987" >PALOCABILDO</option>
<option value="988" >PIEDRAS</option>
<option value="989" >PLANADAS</option>
<option value="990" >PRADO</option>
<option value="991" >PURIFICACION</option>
<option value="992" >RIOBLANCO</option>
<option value="993" >RONCESVALLES</option>
<option value="994" >ROVIRA</option>
<option value="995" >SALDAÑA</option>
<option value="996" >SAN ANTONIO</option>
<option value="997" >SAN LUIS</option>
<option value="998" >SANTA ISABEL</option>
<option value="999" >SUAREZ</option>
<option value="1000" >VALLE DE SAN JUAN</option>

  </select>
      <br />
      <p>¿Eres agricultor?</p>
      <input type="radio" name="rol" value="Agricultor" v-model="user.rol_user"/>
      <label>Sí, quiero mostrar mis productos</label>
      <br />
      <input type="radio" name="rol" value="Vendedor"  v-model="user.rol_user"/>
      <label>No, soy comerciante</label>
      <br />
      <button type="submit">Registrarse</button>
    </form>
  </div>

</template>

<script>
import axios from 'axios';
export default {
  name: "SignUp",
  data: function () {
    return {
      user: {
        id:"",
        usersname: "",
        name_user: "",
        lastname_user: "",
        email: "",
        address_user: "",
        id_city: "",
        num_phone: "",
        password: "",
        sex_user: "",
        rol_user: "",
      },
    };
  },
  methods: {
    processSignUp: function () {
      axios
        .post("https://ciclo3grupo2agroclicbd.herokuapp.com/user/", this.user, {
          headers: {},
        })
        .then((result) => {
          let dataSignUp = {
            id: this.user.id,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
          };
          this.$emit("CompletedSignUp", dataSignUp);
        })
        .catch((error) => {
          console.log(error);
          alert("Ha ocurrido un error en el registro");
        });
    },
  },
};
</script>

<style>
body{
    margin: 0 0 0 0;
    box-sizing: border-box;
  }
form{
  width:400px;
  padding: 16px;
  border-radius: 10px;
  margin:auto;
  background-color:mediumaquamarine;
  margin-top: 20px;
}
form h3{
  height: 0;
  padding: 0%;
}
form input[type="text"],form input[type="email"],form input[type="tel"], form input[type="password"],select{
  width: 300px;
  padding:3px 10px;
  border:1px solid white;
  border-radius: 3px;
  background-color: #f6f6f6;
  margin:8px 0;
  display: inline-block;
}
form input[type="radio"]{
    width: 200px;
  font-style:italic;
}
form button{
  width:100%;
  padding: 8px 16px;
  margin-top: 28px;
  border-radius: 5px;
  border:1px solid #000;
  display: block;
  color:white;
  background-color: #000;
}
form button:hover{
  cursor:pointer;
}
textarea{
  width:100%;
  height: 100px;
  border:1px solid #f6f6f6;
  margin:8px 0;
  resize: none;
  display: block;
}
</style>