---
title: "Una torsione magnetica che orienta la luce"
date: 2026-10-06T09:00:00+02:00
description: "Gli altermagneti sono magneti che nascondono il proprio magnetismo. Quando il loro ordine magnetico si avvolge a spirale, assorbono la luce soprattutto in una polarizzazione. La direzione preferita ruota di 90 gradi al cambiare della frequenza. Il mio nuovo articolo su Physical Review Letters."
hero: hero.png
menu:
  sidebar:
    name: Una torsione magnetica che orienta la luce
    identifier: twist-steers-light
    parent: r_posts
    weight: 10
tags: ["altermagneti", "magnetismo", "ottica", "spintronica"]
categories: ["ricerca"]
---

Prova a guardare il telefono con un paio di occhiali da sole polarizzati e a ruotarlo lentamente.
Su molti telefoni, a un certo punto lo schermo si oscura.
Il motivo è che lo schermo emette luce polarizzata: il campo elettrico della luce
oscilla lungo una direzione precisa. Le lenti degli occhiali lasciano passare
la luce polarizzata in una direzione e assorbono quella polarizzata nella direzione
perpendicolare. Basta quindi ruotare il telefono fino a trovare l'angolo giusto:
la luce dello schermo viene assorbita dalle lenti e non arriva più ai tuoi occhi.

Ora immagina un materiale che faccia la stessa cosa, ma che cambi la direzione
che assorbe a seconda del colore della luce: una per le frequenze più basse,
come il rosso, e una ruotata di novanta gradi per quelle più alte, come il blu.
Un comportamento del genere può rivelare una forma di magnetismo che di solito
passa inosservata.

È l'idea al centro del mio nuovo articolo,
[*Emergent Gauge Fields and Linear Dichroism in Spin-Textured Altermagnets*](https://doi.org/10.1103/phr7-1zy5),
appena pubblicato su *Physical Review Letters*. Vediamo come funziona.

## Magneti che si nascondono

Quando pensiamo a un magnete, ci vengono in mente la calamita sul frigorifero
o l'ago di una bussola. Sono esempi di ferromagneti.
Al loro interno, ogni atomo magnetico si comporta come una minuscola calamita:
ha quello che i fisici chiamano un *momento magnetico*.
Il magnetismo nasce dagli elettroni, che si comportano a loro volta come piccole
calamite grazie a una proprietà chiamata *spin*. Possiamo immaginarlo come una
freccia che punta verso l'alto o verso il basso.
In un ferromagnete, i momenti magnetici sono tutti allineati e i loro effetti
si sommano. È così che si produce il campo magnetico capace di attirare le graffette.

Negli antiferromagneti, invece, i momenti degli atomi vicini puntano in versi
opposti e si compensano. Il campo esterno viene così a mancare.
Questi materiali sono molto più comuni dei ferromagneti, ma anche più difficili
da sfruttare: le due direzioni dello spin risultano indistinguibili sia dall'esterno
sia per gli elettroni che si muovono nel materiale.

Gli **altermagneti**, riconosciuti come una famiglia a sé solo negli ultimi anni,
combinano caratteristiche di entrambi.
Anche qui i momenti si alternano e si compensano, senza produrre un campo esterno.
Gli atomi con momenti opposti, però, non hanno lo stesso ambiente circostante:
le loro disposizioni sono ruotate l'una rispetto all'altra. Per gli elettroni,
questa differenza conta. In un altermagnete, lo spin preferito dipende dalla
*direzione in cui l'elettrone si muove*.

{{< img src="/posts/research_post/magnetic-twist-steers-light/three-magnets.svg" title="Ferromagnete, antiferromagnete e altermagnete a confronto" width="600" align="center" >}}
*In alto: gli atomi magnetici. Nell'altermagnete, i due tipi di atomo sono circondati da strutture
(in grigio) ruotate di 90 gradi l’una rispetto all’altra. In basso: gli elettroni.
Ogni sfera lilla chiaro rappresenta un elettrone che si allontana dal centro lungo una
scia grigia, e la freccia che la attraversa indica il suo spin (le doppie frecce grigie
indicano entrambi gli spin in ugual misura). Nell'altermagnete, gli elettroni che si muovono
lungo una diagonale hanno spin verso l'alto, quelli lungo l'altra verso il basso.*

Gli altermagneti offrono quindi una proprietà utile dei ferromagneti — elettroni
con uno spin preferito — senza il problema del campo esterno. Nelle memorie magnetiche,
quel campo può far interferire tra loro i bit quando sono troppo vicini.

Questo spiega l'interesse per gli altermagneti, oggi tra i temi più studiati nella
fisica della materia condensata. Indizi sperimentali sono stati trovati in materiali
come RuO₂, MnTe e Mn₅Si₃. In una famiglia di composti stratificati del vanadio,
il legame tra spin e direzione del moto è stato osservato anche a temperatura ambiente.

Ma proprio l'assenza di un campo esterno rende difficile riconoscerli.

## I magneti reali si attorcigliano

Fin qui abbiamo immaginato magneti perfettamente ordinati. Nei cristalli reali,
però, l'orientamento dei momenti magnetici può cambiare da un punto all'altro.
Possono esserci zone orientate in modo diverso, separate da confini sottili
in cui i momenti ruotano gradualmente. Oppure possono formarsi spirali:
spostandosi nel materiale, la direzione dei momenti cambia poco alla volta,
come quando si salgono i gradini di una scala a chiocciola.
Esistono anche configurazioni più intricate, come vortici e piccoli nodi chiamati skyrmioni.
L'insieme di questi disegni prende il nome di *texture magnetiche*.

Negli antiferromagneti sono molto comuni: non c'è un campo esterno che ne renda
costosa la formazione in termini di energia. I microscopi le hanno già osservate
anche in materiali candidati a essere altermagneti.

Un altermagnete ha però delle direzioni preferite già fissate dalla struttura
cristallina: gli assi del reticolo quadrato e le diagonali lungo cui gli elettroni
preferiscono uno spin o l'altro. Una torsione aggiunge un'altra direzione,
quella lungo cui i momenti ruotano.

Da qui la domanda del mio lavoro: *come cambia il comportamento degli elettroni
quando l'ordine magnetico ruota lentamente nello spazio? A prevalere è la direzione
del cristallo o quella della torsione?*

## Seguire la torsione

Per affrontare il problema, possiamo cambiare punto di vista.
Immagina di seguire un elettrone nel materiale e di girare la testa man mano
che cambia la direzione dei momenti magnetici. Se ruoti insieme a loro,
li vedi sempre orientati allo stesso modo: il magnete ti appare uniforme.

Questo cambio di prospettiva ha però delle conseguenze, un po' come quando sali
su una giostra. Dal tuo posto, ciò che ruota insieme a te sembra fermo,
ma ti senti spinto verso l'esterno anche se nessuno ti spinge.
E se fai rotolare una palla in linea retta sulla piattaforma, la vedi deviare.
Sono gli effetti della forza centrifuga e della forza di Coriolis:
forze apparenti che compaiono perché stai osservando il moto da un sistema che ruota.
La deviazione della palla dipende dalla sua velocità e dalla direzione in cui si muove.

Per l'elettrone succede qualcosa di simile. Più velocemente si sposta lungo
la torsione, più in fretta deve ruotare il sistema di riferimento per seguire
i momenti magnetici. L'effetto aggiuntivo dipende quindi dalla velocità
dell'elettrone, dalla direzione del suo moto e da quanto rapidamente cambia
l'orientamento dei momenti nello spazio.

{{< img src="/posts/research_post/magnetic-twist-steers-light/gauge-field.svg" title="Elettroni in un magnete attorcigliato, visti dal laboratorio e da un sistema di riferimento che allinea tutti gli spin" width="620" align="center" >}}
*Due punti di vista sugli stessi elettroni. Nel laboratorio, il magnete si attorciglia
e le bussole degli elettroni restano ferme. Passando al sistema di riferimento che segue i momenti magnetici,
tutti gli spin vengono allineati, comprese le bussole. Seguendo la torsione, il magnete appare uniforme,
ma ora le bussole ruotano mentre gli elettroni si muovono: in modo continuo lungo
la torsione (arco verde), per niente nella direzione trasversale.
A questa rotazione corrisponde il campo aggiuntivo.*

Questo effetto si descrive con un **campo di gauge emergente**.
Il nome è tecnico, ma l'idea è quella della giostra.
Il campo è *emergente* perché non viene introdotto da un'altra sorgente:
compare nelle equazioni quando passiamo al sistema di riferimento che segue
i momenti magnetici. Si chiama *campo di gauge* perché entra nelle equazioni
dell'elettrone in modo analogo ai campi elettrici e magnetici.

Il cambio di riferimento si può fare per qualsiasi magnete.
Negli altermagneti, però, il campo agisce sul legame tra spin e direzione del moto.
È questo a fare la differenza. In un normale antiferromagnete, le due direzioni
dello spin sono equivalenti: il campo modifica comunque il moto degli elettroni,
ma non dà origine all'effetto ottico che vedremo tra poco.

## La luce sceglie una direzione

Per osservare questi effetti possiamo usare la luce polarizzata.

Torniamo agli occhiali da sole. I fotografi usano lo stesso principio quando
montano un filtro polarizzatore sull'obiettivo per ridurre i riflessi sull'acqua.
La luce riflessa è in parte polarizzata: ruotando il filtro, il riflesso si attenua
e diventa possibile fotografare ciò che si trova sotto la superficie.

La luce polarizzata permette anche di scoprire proprietà dei materiali che
altrimenti non vedremmo. Prova a mettere un righello di plastica trasparente
davanti allo schermo di un computer e a guardarlo attraverso gli occhiali polarizzati:
vedrai comparire bande colorate. Sono dovute alle tensioni interne rimaste nella
plastica dopo lo stampaggio, che fanno propagare diversamente le due polarizzazioni.

<div style="display: flex; gap: 8px; align-items: flex-start; margin: 1rem 0 0.4rem;">
<img src="/posts/research_post/magnetic-twist-steers-light/polarizer-camera.jpg" alt="Un filtro polarizzatore montato sull'obiettivo di una fotocamera" style="flex: 1.333 1 0%; min-width: 0;">
<img src="/posts/research_post/magnetic-twist-steers-light/polarizer-water.jpg" alt="Lo stesso tratto d'acqua fotografato senza e con un filtro polarizzatore" style="flex: 2.667 1 0%; min-width: 0;">
<img src="/posts/research_post/magnetic-twist-steers-light/photoelastic-protractor.jpg" alt="Un goniometro di plastica tra due polarizzatori, con bande colorate dovute alle tensioni interne" style="flex: 1.333 1 0%; min-width: 0;">
</div>

*A sinistra: un filtro polarizzatore (con la sigla CPL) montato sull'obiettivo.
Al centro: la stessa acqua senza filtro (metà sinistra) e con il filtro (metà destra):
le nuvole riflesse scompaiono e si vede il fondo.
A destra: un goniometro di plastica tra due polarizzatori; i colori mostrano
le tensioni rimaste nella plastica.
Foto da Wikimedia Commons:
[Jonathan Cutrer](https://commons.wikimedia.org/wiki/File:Panasonic_GX8_w_20mm_f_1.7_%26_Gobe_filters_-jcutrer_(44266982721).jpg),
[CC BY 2.0](https://creativecommons.org/licenses/by/2.0/);
[Amithshs](https://commons.wikimedia.org/wiki/File:Reflection_Polarizer2.jpg), pubblico dominio;
[Nevit Dilmen](https://commons.wikimedia.org/wiki/File:Plastic_Protractor_Polarized_05375.jpg),
[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).*

La torsione magnetica produce nell'altermagnete un effetto simile, ma agisce
sull'assorbimento: anziché far propagare le due polarizzazioni a velocità diverse,
come la plastica, ne fa assorbire una più dell'altra.
La torsione rompe la simmetria quadrata del cristallo e dà origine al
**dicroismo lineare**. In pratica, il materiale assorbe molto più intensamente
la luce polarizzata in una direzione rispetto a quella polarizzata nella
direzione perpendicolare, proprio come le lenti degli occhiali.
Nei calcoli la differenza è marcata: su un ampio intervallo di frequenze,
viene assorbita quasi soltanto una delle due polarizzazioni.

La cosa interessante è che un normale antiferromagnete, con la stessa identica
torsione, non può produrre questo assorbimento: la sua simmetria lo impedisce.
Per ottenerlo bisogna aggiungere l'accoppiamento spin-orbita, un effetto relativistico
che lega lo spin dell'elettrone al suo moto e a cui spesso si ricorre per spiegare
segnali ottici nei magneti. Nell'altermagnete, invece, non serve.

Misurare quanta luce viene assorbita nelle diverse polarizzazioni può quindi
servire sia a osservare la torsione sia a capire se il materiale è un altermagnete.

## Una rotazione di novanta gradi

Ma qual è la direzione in cui viene assorbita più luce? È qui che emerge il risultato più curioso.

{{< img src="/posts/research_post/magnetic-twist-steers-light/axis-vs-frequency.svg" title="Dicroismo lineare e direzione di assorbimento in funzione della frequenza, calcolati con il modello" width="560" align="center" >}}
*Calcolo con il modello dell'articolo per una spirale inclinata di 22,5 gradi rispetto
a un asse del cristallo. In alto: quanto l'assorbimento favorisce una polarizzazione.
In basso: la direzione di massimo assorbimento. A bassa frequenza resta fissata a
un asse del cristallo; al passaggio tra i due regimi ruota di 90 gradi,
poi si orienta verso una direzione determinata dalla torsione (linea verde tratteggiata).*

Alle basse frequenze, la direzione di massimo assorbimento resta **fissa rispetto
al cristallo**: coincide con uno dei suoi assi, indipendentemente dalla direzione
della torsione. Aumentando la frequenza si arriva a un punto di passaggio:
le due polarizzazioni vengono assorbite quasi allo stesso modo e la direzione
preferita ruota di novanta gradi.

Alle frequenze più alte, invece, la direzione di assorbimento **segue la torsione**.
Più precisamente, tende alla direzione che si ottiene riflettendo quella della
torsione rispetto alla diagonale del cristallo.

I due comportamenti ci dicono cose diverse. A bassa frequenza otteniamo un segnale
chiaro della presenza di una torsione; ad alta frequenza possiamo ricavarne
anche la direzione. La frequenza a cui avviene il passaggio dipende dall'intensità
dell'altermagnetismo e dal passo della torsione.

Per gli altermagneti stratificati studiati oggi in laboratorio, considerando
texture delle dimensioni già osservate, il passaggio tra i due regimi cade
tra i terahertz e il medio infrarosso. È un intervallo accessibile alle normali
misure spettroscopiche con luce polarizzata. I «colori» di cui parliamo qui,
quindi, sono fuori dalla gamma visibile ai nostri occhi.

L'immagine qui sotto riassume i due casi. Due fasci di luce, uno a bassa e uno
ad alta frequenza, attraversano una lastra di altermagnete con una torsione magnetica.
Entrambi arrivano con due polarizzazioni: una viene assorbita, l'altra attraversa
il materiale. L'onda più tenue rappresenta la componente che si spegne nel cristallo.
I quadranti accanto ai fasci in uscita mostrano la polarizzazione trasmessa vista
di fronte: nel primo caso è orientata secondo un asse del cristallo,
nel secondo secondo una direzione determinata dalla torsione.

{{< img src="/posts/research_post/magnetic-twist-steers-light/slab-polarizer.svg" title="Una lastra di altermagnete attorcigliato lascia passare polarizzazioni diverse a bassa e ad alta frequenza" width="500" align="center" >}}
*Lo stesso altermagnete attorcigliato, due colori della luce:
a bassa frequenza la polarizzazione che passa è fissata dal cristallo,
ad alta frequenza dalla torsione.*

## Perché conta

Questo risultato apre tre possibilità che trovo particolarmente interessanti.

**Osservare un magnetismo difficile da vedere.**
Le tecniche usate per studiare i magneti ordinari ci dicono poco sugli altermagneti.
La luce polarizzata potrebbe permetterci di ricostruire le loro texture senza
toccare il campione, con un apparato da laboratorio relativamente compatto.
La rotazione della direzione di assorbimento al passaggio tra i due regimi
fornisce un segnale caratteristico, difficile da riprodurre con altri meccanismi.

**Riconoscere un altermagnete.**
L'effetto scompare in un normale antiferromagnete con la stessa torsione:
ci aiuta quindi a distinguere materiali che, da fuori, possono sembrare uguali.
Il risultato resta valido anche in presenza del debole accoppiamento spin-orbita
dei materiali reali. Questo, anzi, aggiunge un'informazione, perché permette
di riconoscere anche il senso in cui si avvolge la torsione.

**Controllare le proprietà del materiale.**
Possiamo anche guardare il risultato dall'altro lato. La torsione modifica
l'assorbimento della luce, ma anche la conduzione elettrica: nell'articolo mostro
che ne risentono anche le correnti continue. Creare una torsione nel materiale
potrebbe quindi essere un modo per regolarne le proprietà ottiche ed elettroniche
lungo le direzioni desiderate.

Per ora si tratta di una previsione teorica: sarà l'esperimento a dirci se funziona.
La prova consiste nell'illuminare un altermagnete con una torsione magnetica usando
luce polarizzata nei terahertz o nell'infrarosso. Ruotando la polarizzazione
si può individuare la direzione di massimo assorbimento e verificare se ruota
di novanta gradi quando si aumenta la frequenza.

---

**L'articolo:** A. Maiani, *Emergent Gauge Fields and Linear Dichroism in Spin-Textured
Altermagnets*, Phys. Rev. Lett. **137**, 136703 (2026),
[doi:10.1103/phr7-1zy5](https://doi.org/10.1103/phr7-1zy5).
Una versione gratuita è disponibile su [arXiv:2602.14950](https://arxiv.org/abs/2602.14950).

**Codice e dati:** tutto ciò che serve per riprodurre le figure dell'articolo
è disponibile liberamente su Zenodo,
[doi:10.5281/zenodo.18658428](https://doi.org/10.5281/zenodo.18658428).

*Questo lavoro è stato finanziato dalla Wallenberg Initiative on Networks and Quantum Information.*
