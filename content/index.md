# Table of Contents

<div class="toc"><ul>
  <li><a href="index.html">Introduction</a> &ndash; this page</li>
  <li><a href="a4000-bom.html">The Bill of Material</a> &ndash; what you are probably here for</li>
  <li><a href="csv.html">CSV Export</a> &ndash; for Mouser Electronics</li>
  <li><a href="a4000-bom.xlsx">Excel Export</a> &ndash; for your spreadsheet application</li>
  <li><a href="https://github.com/shred/a4000-bom">GitHub Project Page</a> &ndash; feel free to contribute</li>
</ul></div>

# Introduction

This is the Bill of Material for a replica Amiga 4000D Rev B. It is optimized for [Acill's A4000 Replica Project](https://github.com/Acill/A4000RevB) boards.

## Read Me First!

If you want to build your own Amiga, be aware that the machine was designed in the early 1990s.

While almost all of the standard components are still available, some components are very rare by now. You will need *all* of the listed components (except of those marked optional). We recommend that you try to get the components marked as <span class="rare">Rare</span> first, so you won't waste your money on standard components if you fail to get all the rare ones.

Also be aware that there are six PALs that need to be programmed. While the JEDEC files are [available at the Amiga Wiki](http://www.amigawiki.de/doku.php?id=en:parts:pld_download#a4000), a GAL capable programmer is required for "flashing" the corresponding GALs. They cannot be programmed in-circuit.

As the Amiga mainboard does not comply to the ATX form factor, you cannot use a standard PC case and a PC power supply without careful selection and manual changes.

This bill of material only comprises of the components required for the mainboard itself. **The absolute bare minimum for a booting machine is:**

* This mainboard, fully assembled and tested
* A power supply (and a Mate-N-Lok connector/adapter unless an original PSU is used)
* A CPU board
* One 2MB SIMM module (**double** sided) for Chip RAM

For a complete Amiga 4000D you also need:

* A computer case (and the skills to make it fit unless it's the original case)
* Up to four 4MB SIMM modules (**single** sided) for Fast RAM
* An Amiga 4000 daughterboard
* An Amiga keyboard and Amiga mouse
* Hard disk drives and floppy disk drives at your discretion

For the SIMMs, standard PS/2 72-pin modules can be used (FPM or EDO, parity bit on 36 bit SIMMs will be ignored). Access time must be 80ns or faster. For the Fast RAM 60ns modules should be preferred, as the Amiga can be switched to 60ns access time via software. See [this article](http://amigadev.elowar.com/read/ADCD_2.1/AmigaMail_Vol2_guide/node0162.html) for more details about suitable SIMM types.

## Battery and Capacitors

This Bill of Material includes a NiCd battery as buffer for the RTC. These batteries tend to leak over the years, and certainly killed a lot of classic Amiga 4000s. It is advisable to use a different type of energy source, like a button cell. However, the necessary components and modifications are *not* part of this project.

This list also includes regular electrolytic capacitors, which may leak and cause damage over the years as well. Some people prefer to use ceramic capacitors instead. They cannot leak, but *may* cause other problems. There are good arguments on both sides, so the final choice is up to you. However, if you decide to use electrolytic capacitors, we recommend to get polymer hybrid aluminum electrolytic capacitors (if possible), and generally get the best quality that money can buy.

## U103

For most cases, U103 needs to be populated with an 74FCT244T. However, some CPU boards (e.g. A3640 Rev 3.0) require a 74FCT240 here instead. It is recommended to use a socket for this chip, so it can easily be exchanged. Symptom for a wrong chip type is that the Amiga only shows a black screen and won't start at all, while it works perfectly with other CPU boards.

## Sockets

This list contains sockets for all chips in DIP and PLCC packages for your convenience. It is of course up to you if you want to use all of them.

On an original Amiga 4000D board, only U103, U175, U176, and U700 are socketed. It may also be helpful to use sockets for all GAL chips, as they may need to be reprogrammed if it should turn out that a wrong JEDEC file was used.

It is disputed if all custom chips should be seated in PLCC sockets. On the one hand, it would not be needed to solder in the rare custom chips, and it would also be easy to remove them later. On the other hand, there may be signal problems caused by the sockets that may be hard to trace.

Also note that the sockets of U700 and U714 are very close together. It might be difficult to solder in both of them correctly.

## Disclaimer

This is not an official list! It was collected and reviewed by Amiga enthusiasts.

Although we strive to make the information in this project as helpful and accurate as possible, it is provided "as is" and without warranties of any kind either expressed or implied.

In other words: You might spend a lot of money, and end up with a non-functioning mainboard or a cardboard box full of useless components.

**Use at your own risk!**

## Sources

The following sources have been used:

* AmigaWiki: [A4000 Rev B Schematic](http://www.amigawiki.de/dnl/schematics/A4000_Rb.pdf)
* Acill: [A4000 Replica Project](https://github.com/Acill/A4000RevB)
* Chucky: [Component Locator, A4000 RevB - Acill](http://locator.reamiga.info/locator.php?project=A4000)
* Shred's classic Amiga 4000D mainboard

## Contribute

This list is meant to be a community work. Our goal is to have a canonical list that people can rely on when ordering parts for building an own Amiga 4000D mainboard.

However, this list may not be free of errors. If you have found one, please [open an issue](https://github.com/shred/a4000-bom/issues), send a patch, or [send me a message](https://www.a1k.org/forum/index.php?members/6632/) at the A1K.org forum.

## License

This project is distributed under the terms of [GNU General Public License (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.en.html#content).
