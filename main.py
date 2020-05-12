#!/usr/bin/env python
import utils
import Globals
import features
import slicers
import vectorizer


def main():
    Globals.setup()
    Globals.logger.info(' ======  Started ======')
    run()
    Globals.logger.info(' ======  Finished ======')
    Globals.destroy()


def run():
    sample_path = Globals.config['Dataset']['test_sample']
    files = utils.get_files(sample_path)

    # ======================= FEATURE EXTRACTION START =======================
    for filename in files:
        # START - extract vulnerable statements for SARD Dataset
        if Globals.config['Vulnerable Statements']['SARD']:
            flaws, line_numbers, flaw_descriptions = features.find_vulnerable_statements(filename)
            for (flaw, line_number, flaw_description) in zip(flaws, line_numbers, flaw_descriptions):
                # print(flaw, line_number, flaw_description)
                Globals.logger.info(str(line_number) + ": " + str(flaw))
        # END - extract vulnerable statements for SARD Dataset

        # START - slicer
        sliced_program = run_slicer(filename)
        # END - slicer

        # START - vectorizer
        vector = run_vectorizer(sliced_program)
        # END - vectorizer

        # START - dump extracted data
        # END - dump extracted data

    # ======================= FEATURE EXTRACTION END =======================

    # START - load extracted data
    # END - load extracted data

    # START - train
    # END - train

    # START - test
    # END - test

    # START - result & summary
    # END - result & summary

    # START - analysis & visualization
    # END - analysis & visualization


def run_slicer(filename):

    sliced_program = []
    # START - backward slicer
    if Globals.config['Slicer']['backward-slicer']:
        Globals.logger.info("Backward Slicer Running for " + filename)
        sliced_program = slicers.backward_slicer(filename)
    # END - backward slicer

    # START - dg slicer
    elif Globals.config['Slicer']['dg-slicer']:
        print(Globals.config['Slicer']['dg-slicer'])
        Globals.logger.info("dg Slicer Running for " + filename)
        sliced_program = slicers.dg_slicer(filename)
    # END - backward slicer

    # START - C-Code-Slicer
    elif Globals.config['Slicer']['C-Code-Slicer']:
        Globals.logger.info("C-Code-Slicer Running for " + filename)
        sliced_program = slicers.c_code_slicer_slicer(filename)
    # END - C-Code-Slicer

    return sliced_program


def run_vectorizer(sliced_program):
    # START - vectorizer
    vectors = []
    if Globals.config['Vectorizer']['word2vec']:
        Globals.logger.info("word2vec Running ... ")
        print("sliced_program:" , sliced_program)
        vectors = vectorizer.code2vec(sliced_program)
    # END - vectorizer
    return vectors


if __name__ == "__main__":
    main()
