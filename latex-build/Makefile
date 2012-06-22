DOCUMENT = cloud_forensics
DOCUMENT_SRC = $(DOCUMENT).tex
DOCUMENT_BIN = $(DOCUMENT).pdf
#BUILD_TOOL = rubber
#BUILD_TOOL_ARGS = --pdf -f
BUILD_TOOL = latexmk
BUILD_TOOL_ARGS = -pdf
RM = rm

SUBDIRS = 

TEX_DIR = .
PIC_DIR = pic
BIB_DIR = bib

TEX_FILES = \
	$(TEX_DIR)/cloud_forensics.tex \


BIB_FILES = \
	$(BIB_DIR)/sources.bib \


all: pictures
	$(MAKE) $(DOCUMENT_BIN)

$(DOCUMENT).pdf: $(DOCUMENT_SRC) $(TEX_FILES) $(BIB_FILES)
	$(BUILD_TOOL) $(BUILD_TOOL_ARGS) $(DOCUMENT_SRC)

pictures: 
	$(MAKE) -C $(PIC_DIR) pdf

.PHONY: clean all

clean: 
	$(MAKE) -C $(PIC_DIR) clean
	-$(BUILD_TOOL) --clean -f $(DOCUMENT).tex
	-$(RM) -f $(DOCUMENT).pdf *.aux *.dvi *.log *.toc *.out *~ *.backup 
	-$(RM) -f *.snm *.nav *.ist *.glo *.acr *.bbl *.blg *.acn *.fdb_latexmk
	@for dir in $(SUBDIRS); do (cd $$dir; $(MAKE) clean); done

distclean: clean
	$(MAKE) -C $(PIC_DIR) clean
