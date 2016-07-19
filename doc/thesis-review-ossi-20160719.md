These are persistent notes of the [OUSPG open](https://github.com/ouspg/ouspg-open) review of the draft of [Ossi Herrala's secudep](https://github.com/ouspg/secudep/blob/master/thesis/thesis.pdf) on [etherpad](http://muistio.tieke.fi/p/secudep) [11 reviewers]

# Generic notes

 * Few small typos which Word finds easily :-)
 * Research question, methodology, scope
 * Metatext "This thesis is structured as follows, ..." "In this chapter, ..."
 * In LaTeX ~\cite{foo} does the right thing (non-breaking space), style guide says to use a space before bracket.
 * DFD based threat model with trust boundaries could be a very good way for explaining the system, especially since you're systematically mitigating them? Using STRIDE?
 * Configuration files etc. should be put in an appendix

Be careful with syllabication
"Tavutus. Latex tavuttaa tekstin automaattisesti. Tavalliset suomenkieliset sanat menevät kyllä yleensä oikein, mutta yhdyssanojen ja vierasperäisten sanojen kohdalla Latex voi erehtyä."

# ABBREVIATIONS

UDP user datagram protocol -> User Datagram Protocol (others are written with first capital letters too)

> MITM

 * Casing: MitM

# 1. INTRODUCTION

> Usually network installation systems are built to serve single organization (e.g. uni- versity department or single business) to achieve repeatable and homogeneous instal- lations. For example school’s computer class wants to have identical installations on all machines and reinstalling the machines should be as simple and as fast as possible.

 * This explains current mainstream thinking BUT should this be followed with some sort of bridge to the real context of this work? Or are you actually that interest in classrooms
  * Classic intro goes like (context at large, what is the problem to be solved, what others have done to solve it, what is the gap, what did you do)
 * This work mentions later the distributed installation (search: "but things can shift more towards")

 * Fixes
  * "...where small image is used.." ->"...where  a small image is used.."
  * "...into state where..." -> "...into a state where..."

## 1.2. Current state

Would benefit from an illustration with somesort of highlighting of what is obsolete and not suitable and which parts are ok'ish and usable in current state.

> However, these protocols are not secure and should not be used over Internet.

 * Soon, in next chapter you reason that not even the LANs are safe, so that makes this sentence actually just confusing here since with next argument the
 Internet loses its special meaning

2. Implementing something
encouraces -> encourages

> 1.3 Connections in Internet doesn’t see national

 * do not?

> Same problems can also be present in networks like corporate intranets,

 * Corporate intranets nowadays span over Internet as well - and not securely -> intranet = Internet at the end of the day

> moves there laterally

 * Might be too profession-specific language, should it use more common language?

> Tanenbaum’s Computer Networks[10] divides network security threats into four categories:
> secrecy, authentication, nonrepudiation and integrity control.

 * Any reason to mention this over CIA (- confidentiality, integrity, availability)? -I Agree on this one. i would also prefer CIA
  * Secrecy (or data confidentiality)    -> C
  * Authentication ensures receiving, transimitting ... -> C
  * Integrity control guarantees that ... -> I
   * Nonrepudiation ensures proof of integrity and the origin of data -> I
  * And the A is missing?

> That however requires

 * That, however, requires ?

> no need to changes

  * No need for changes ?

> The backdoors could have been installed already on factory or firmware was infected with some malware previously ran on the machine

 * .. or firmware could have been infected with some...

> Boot environment is loaded from trusted media, for example using prebuilt USB mass media.

 * Do you need to comment the physical security of the used media. (or tampering of media). Or counted as out-of-scope (HWish..)
 * This was dealt with after few sentences. Quick consideration of mentioning this right next to the "booting media"

## 1.4 Threats

* Where is the Table 1.4?

> future communications... etc.
* Maybe the "future" can be removed from these sentences.

 > so there's no need to changes to network...

"There's no need for changes in the" OR "there's no need to change the"  network configuration

 > Threats can be indentified in all components from hardware to operating system vulnerabilities.

 * Risk != Threat != Vulnerablity != Attack

Start of the chapter is confusing. Lets discuss live. I blame Tanenbaum or your interpretation of it. :)

Sure "secrecy" can't be a threat to anyone but oppressive governments?!? :) :)

> threats can be detected  

 * same semantic challenge, see e.g. https://en.wikipedia.org/wiki/Threat_(computer)

# 2. IMPLEMENTING SOMETHING

 * Something? ;)
 * How about "Implementation"?

 >  but things can shift more

  * "things"  -> deployment model can shift to support ... ?  
  * ("things makes the reader pause and start contemplating 'what things')

 * BTW, distributed setups, there you have also the missing A(vailability) consideration ;)


> s learned from boot.foo.sh

 * boot.foo.sh -installation automation service

 > ""no need to have monolithic
 -> "no need to have a monolithic"
 > "Installation infrastructure should help end user achieve fresh installation..."
 -> "Installation infrastructure should help an/the end user achieve a fresh installation..."

# 3 TESTING SOMETHING

## 3.1

> PCAP dump and take a peek inside

  * What is the plan/expected result? Confirm theories about insecure current approaches? Observing your own implementation
   * "Test Something" implies there is no plan yet. By any chance this would not happen to be "select approach first, reason
      later?" :)
