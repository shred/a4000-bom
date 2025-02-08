# Table of Contents

<div class="toc"><ul>
  <li><a href="index.html">Introduction</a> &ndash; this page</li>
  <li><a href="a4000-bom.html">The Bill of Materials</a> &ndash; what you are probably here for</li>
  <li><a href="csv.html">CSV Export</a> &ndash; for Mouser Electronics</li>
  <li><a href="a4000-bom.xlsx">Excel File Download</a> &ndash; for your spreadsheet application</li>
  <li><a href="diffs.html">Known Discrepancies</a> &ndash; in our sources</li>
  <li><a href="https://codeberg.org/shred/a4000-bom">Codeberg Project Page</a> &ndash; feel free to contribute</li>
  <li><a href="other.html">Other Bill of Materials</a> &ndash; if you liked this one</li>
</ul></div>

# Introduction

This is the Bill of Materials for a replica Amiga 4000D Rev B. It is optimized for [Acill's A4000 Replica Project](https://github.com/Acill/A4000RevB) boards.

## Read Me First!

If you want to build your own Amiga, be aware that the machine was designed in the early 1990s.

While almost all the standard components are still available, some components are very rare by now. You will need *all* the listed components (except of those marked optional). We recommend that you try to get the components marked as <span class="rare">Rare</span> first, so you won't waste your money on standard components if you fail to get all the rare ones.

Also be aware that there are six PALs that need to be programmed. They cannot be programmed in-circuit, so you will need a GAL capable programmer.

As the Amiga mainboard does not comply to the ATX form factor, you cannot use a standard PC case and a PC power supply without careful selection and manual changes.

This bill of material includes only the components required for the mainboard itself. **The absolute bare minimum for a booting machine is:**

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

## GALs

The JEDEC files for programming the GALs are [available at the Amiga Wiki](http://www.amigawiki.de/doku.php?id=en:parts:pld_download#a4000).

There is a "PIO2 Mod" that enhances the speed of the internal IDE interface by supporting the PIO2 transfer mode. The patched fusemaps for U901 and U902 can be [found here](https://www.amigawiki.org/doku.php?id=de:projects:pio2mode) (German language only).

Note that classic GALs are no longer produced. In the component list, Atmel ATF16V8B and ATF22V10C are linked as proposed replacement. While the ATF16V8B type is a drop-in replacement that _should_ work, the ATF22V10C is a bit different as it has no internal input pull-up resistors. This _should_ make no difference here, but if you find an affordable ATF22V10**B** type, you should prefer it.

There is no confirmation yet that the Atmel chips are actually working replacements. **If in doubt, use <abbr title="New Old Stock">NOS</abbr> GALs!**

If you use the Atmel chips, we would appreciate your feedback (both positive and negative).

## Electrolytic Capacitors

This list also includes regular electrolytic capacitors, which can leak and cause damage to the board as they age. You should prefer to use capacitors with a higher voltage rating and a maximum temperature of at least 85°C, to extend their lifetime. We recommend getting polymer hybrid aluminum electrolytic capacitors (if possible), and generally get the best quality that money can buy.

Some people prefer to use ceramic or tantalum capacitors instead. They cannot leak, but they have other disadvantages. There are good arguments for and against, so the final choice is up to you.

## Battery

This Bill of Material includes a NiCd battery as buffer for the RTC. These batteries tend to leak over the years, and certainly killed a lot of classic Amiga 4000s.

It is advisable to use a different type of energy source, like a button cell. However, the necessary components and modifications are *not* part of this project.

**Caution:** Do not use a non-rechargeable battery here, without the necessary hardware modifications. There is a danger of fire or explosion.

## U103

For most cases, U103 needs to be populated with an 74FCT244T. However, some CPU boards (e.g. A3640 Rev 3.0) require a 74FCT240 here instead. It is recommended to use a socket for this chip, so it can easily be exchanged. Symptom for a wrong chip type is that the Amiga only shows a black screen and won't start at all, while it works perfectly with other CPU boards.

## Sockets

This list contains sockets for all chips in DIP and PLCC packages for your convenience. It is of course up to you if you want to use all of them.

On an original Amiga 4000D board, only U103, U175, U176, and U700 are socketed. It may also be helpful to use sockets for all GAL chips, as they may need to be reprogrammed if it should turn out that a wrong JEDEC file was used.

It is disputed if all custom chips should be seated in PLCC sockets. On the one hand, it would not be needed to solder in the rare custom chips, and it would also be easy to remove them later. On the other hand, there may be signal problems caused by the sockets that may be hard to trace.

Also note that the sockets of U700 and U714 are very close together. It might be difficult to solder in both of them correctly.

## Acill Board

If you rebuild an Amiga with Acill's replica board, make sure to populate R465. L500 can be left out, as it is not connected anywhere. If R465 is missing, you will get a very dark or even black video signal, because the video DAC has no output reference voltage.

On original Commodore boards, L500 is populated, and R465 is usually left out.

## Disclaimer

This is not an official list! It was collected and reviewed by Amiga enthusiasts.

Although we strive to make the information in this project as helpful and accurate as possible, it is provided "as is" and without warranties of any kind either expressed or implied.

In other words: You might spend a lot of money, and end up with a non-functioning mainboard or a cardboard box full of useless components.

**Use at your own risk!**

## Contribute

This list is meant to be a community work. Our goal is to have a canonical list that people can rely on when ordering parts for building an own Amiga 4000D mainboard.

However, this list may not be free of errors. If you have found one, please [open an issue](https://codeberg.org/shred/a4000-bom/issues), send a patch, or [send me a message](https://www.a1k.org/forum/index.php?members/6632/) at the A1K.org forum.

## License

This project is distributed under the terms of [GNU General Public License (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.en.html#content).
