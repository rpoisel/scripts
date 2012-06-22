#########################################################
#                                                       #
#	Author:   Rainer Poisel                               #
#	Contact:  rainer.poisel@xfreaks.net                   #
#	Date:     01042005                                    #
#	Purpose:	LaTeX - Makefile                            #
#                                                       #
#	Description:	Automating processes                    #
#                                                       #
#########################################################

VECT_FILE_EXT := svg
RAST_FILE_EXT := png
DIA_FILE_EXT := dia
VECT_TO_EPS_TOOL=inkscape
VECT_TO_PNG_TOOL=inkscape
DIA_TO_SVG_TOOL=dia
VECT_TO_EPS_TOOL_FLAGS=--without-gui --export-eps=
VECT_TO_PNG_TOOL_FLAGS=--without-gui --export-dpi=300 --export-area-drawing --export-png=
DIA_TO_EPS_TOOL_FLAGS=-t svg -e
DIAFILES := $(wildcard *.$(DIA_FILE_EXT))
SVGFILES := $(wildcard *.$(VECT_FILE_EXT))
DIASVGFILES := $(patsubst %.$(DIA_FILE_EXT),%.$(VECT_FILE_EXT),$(DIAFILES))
SRCFILES =  $(SVGFILES) $(DIASVGFILES)
PDFFILES := $(patsubst %.$(VECT_FILE_EXT),%.pdf,$(SRCFILES))
PNGFILES := $(patsubst %.$(VECT_FILE_EXT),%.png,$(SRCFILES))
EPSFILES := $(patsubst %.$(VECT_FILE_EXT),%.eps,$(SRCFILES))

EPSTOPDF=epstopdf
RM=rm

all: pdf

png: $(PNGFILES)

pdf: $(PDFFILES)

%.pdf: %.eps
	$(EPSTOPDF) $<

%.eps: %.$(VECT_FILE_EXT)
	$(VECT_TO_EPS_TOOL) $(VECT_TO_EPS_TOOL_FLAGS)$(patsubst %.$(VECT_FILE_EXT),%.eps,$<) $<

%.png: %.$(VECT_FILE_EXT)
	$(VECT_TO_PNG_TOOL) $(VECT_TO_PNG_TOOL_FLAGS)$(patsubst %.$(VECT_FILE_EXT),%.png,$<) $<

%.svg: %.$(DIA_FILE_EXT)
	$(DIA_TO_SVG_TOOL) $(DIA_TO_EPS_TOOL_FLAGS) $(patsubst %.$(DIA_FILE_EXT),%.$(VECT_FILE_EXT),$<) $<
	
.PHONY: clean

clean: 
	-$(RM) $(PDFFILES) $(EPSFILES) $(PNGFILES) $(DIASVGFILES)
	-$(RM) *.$(VECT_FILE_EXT)~ *.$(DIA_FILE_EXT)~
	-$(RM) Thumbs.db
