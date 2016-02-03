# -*- coding: utf-8 -*-
"""
Unittests for tellurium.py
Main module for tests.
"""
from __future__ import print_function, division
import unittest
import tellurium as te

import os
import numpy as np
test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testdata')


class TelluriumTestCase(unittest.TestCase):
    def setUp(self):
        # switch the backend of matplotlib, so plots can be tested
        import matplotlib
        matplotlib.pyplot.switch_backend("Agg")

        self.ant_str = '''
        model pathway()
             S1 -> S2; k1*S1

             # Initialize values
             S1 = 10; S2 = 0
             k1 = 1
        end
        '''
        self.sbml_str = '''<?xml version="1.0" encoding="UTF-8"?>
        <!-- Created by libAntimony version v2.8.1 on 2016-02-02 11:45 with libSBML version 5.12.1. -->
        <sbml xmlns="http://www.sbml.org/sbml/level3/version1/core" xmlns:comp="http://www.sbml.org/sbml/level3/version1/comp/version1" level="3" version="1" comp:required="true">
          <model id="pathway" name="pathway">
            <listOfCompartments>
              <compartment sboTerm="SBO:0000410" id="default_compartment" spatialDimensions="3" size="1" constant="true"/>
            </listOfCompartments>
            <listOfSpecies>
              <species id="S1" compartment="default_compartment" initialConcentration="10" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
              <species id="S2" compartment="default_compartment" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
            </listOfSpecies>
            <listOfParameters>
              <parameter id="k1" value="1" constant="true"/>
            </listOfParameters>
            <listOfReactions>
              <reaction id="_J0" reversible="true" fast="false">
                <listOfReactants>
                  <speciesReference species="S1" stoichiometry="1" constant="true"/>
                </listOfReactants>
                <listOfProducts>
                  <speciesReference species="S2" stoichiometry="1" constant="true"/>
                </listOfProducts>
                <kineticLaw>
                  <math xmlns="http://www.w3.org/1998/Math/MathML">
                    <apply>
                      <times/>
                      <ci> k1 </ci>
                      <ci> S1 </ci>
                    </apply>
                  </math>
                </kineticLaw>
              </reaction>
            </listOfReactions>
          </model>
        </sbml>
        '''

        self.cellml_str = '''<?xml version="1.0"?>
        <model xmlns:cellml="http://www.cellml.org/cellml/1.1#" xmlns="http://www.cellml.org/cellml/1.1#" name="pathway">
        <component name="pathway">
        <variable initial_value="10" name="S1" units="dimensionless"/>
        <variable initial_value="0" name="S2" units="dimensionless"/>
        <variable initial_value="1" name="k1" units="dimensionless"/>
        <variable name="_J0" units="dimensionless"/>
        <math xmlns="http://www.w3.org/1998/Math/MathML">
        <apply>
        <eq/>
        <ci>_J0</ci>
        <apply>
        <times/>
        <ci>k1</ci>
        <ci>S1</ci>
        </apply>
        </apply>
        </math>
        <variable name="time" units="dimensionless"/>
        <math xmlns="http://www.w3.org/1998/Math/MathML">
        <apply>
        <eq/>
        <apply>
        <diff/>
        <bvar>
        <ci>time</ci>
        </bvar>
        <ci>S1</ci>
        </apply>
        <apply>
        <minus/>
        <ci>_J0</ci>
        </apply>
        </apply>
        </math>
        <math xmlns="http://www.w3.org/1998/Math/MathML">
        <apply>
        <eq/>
        <apply>
        <diff/>
        <bvar>
        <ci>time</ci>
        </bvar>
        <ci>S2</ci>
        </apply>
        <ci>_J0</ci>
        </apply>
        </math>
        </component>
        <group>
        <relationship_ref relationship="encapsulation"/>
        <component_ref component="pathway"/>
        </group>
        </model>
        '''

        self.ant_file = os.path.join(test_dir, 'models', 'example1')
        self.sbml_file = os.path.join(test_dir, 'models', 'example1.xml')
        self.cellml_file = os.path.join(test_dir, 'models', 'example1.cellml')

    # ---------------------------------------------------------------------
    # Loading Models Methods
    # ---------------------------------------------------------------------
    def test_loada_file(self):
        r = te.loada(self.ant_file)
        self.assertIsNotNone(r)

    def test_loada_str(self):
        r = te.loada(self.ant_str)
        self.assertIsNotNone(r)

    def loadAntimonyModel_file(self):
        r = te.loadAntimonyModel(self.ant_file)
        self.assertIsNotNone(r)

    def loadAntimonyModel_str(self):
        r = te.loadAntimonyModel(self.ant_str)
        self.assertIsNotNone(r)

    def test_loadSBMLModel_file(self):
        r = te.loadSBMLModel(self.sbml_file)
        self.assertIsNotNone(r)

    def test_loadSBMLModel_str(self):
        r = te.loadSBMLModel(self.sbml_str)
        self.assertIsNotNone(r)

    def loadCellMLModel_file(self):
        r = te.loadCellMLModel(self.cellml_file)
        self.assertIsNotNone(r)

    def loadCellMLModel_str(self):
        r = te.loadCellMLModel(self.cellml_str)
        self.assertIsNotNone(r)

    # ---------------------------------------------------------------------
    # Interconversion Methods
    # ---------------------------------------------------------------------
    def test_antimonyToSBML_file(self):
        sbml = te.antimonyToSBML(self.ant_file)
        self.assertIsNotNone(sbml)

    def test_antimonyToSBML_str(self):
        sbml = te.antimonyToSBML(self.ant_str)
        self.assertIsNotNone(sbml)

    def test_antimonyToCellML_file(self):
        cellml = te.antimonyToCellML(self.ant_file)
        self.assertIsNotNone(cellml)

    def test_antimonyToCellML_str(self):
        cellml = te.antimonyToCellML(self.ant_str)
        self.assertIsNotNone(cellml)

    def test_sbmlToAntimony_file(self):
        ant = te.sbmlToAntimony(self.sbml_file)
        self.assertIsNotNone(ant)

    def test_sbmlToAntimony_str(self):
        ant = te.sbmlToAntimony(self.sbml_str)
        self.assertIsNotNone(ant)

    def test_sbmlToCellML_file(self):
        cellml = te.sbmlToCellML(self.sbml_file)
        self.assertIsNotNone(cellml)

    def test_sbmlToAntimony_str(self):
        cellml = te.sbmlToCellML(self.sbml_str)
        self.assertIsNotNone(cellml)

    def test_cellmlToAntimony_file(self):
        ant = te.cellmlToAntimony(self.cellml_file)
        self.assertIsNotNone(ant)

    def test_cellmlToAntimony_str(self):
        ant = te.cellmlToAntimony(self.cellml_str)
        self.assertIsNotNone(ant)

    def test_cellmlToSBML_file(self):
        sbml = te.cellmlToSBML(self.cellml_file)
        self.assertIsNotNone(sbml)

    def test_cellmlToSBML_str(self):
        sbml = te.cellmlToSBML(self.cellml_str)
        self.assertIsNotNone(sbml)

    # ---------------------------------------------------------------------
    # Simulate options
    # ---------------------------------------------------------------------
    # def test_simulateOptions_steps(self):
    #     r = te.loada(self.ant_str)
    #     self.assertRaises(DeprecationWarning, r.setSteps, 200)
    #     self.assertRaises(DeprecationWarning, r.getSteps)
    #     # r.setSteps(200)
    #     # steps = r.getSteps()
    #     # self.assertEqual(200, steps)
    #
    # def test_simulateOptions_numberOfPoints(self):
    #     r = te.loada(self.ant_str)
    #     self.assertRaises(DeprecationWarning, r.setNumberOfPoints, 500)
    #     self.assertRaises(DeprecationWarning, r.getNumberOfPoints)
    #     # r.setNumberOfPoints(500)
    #     # steps = r.getSteps()
    #     # numberOfPoints = r.getNumberOfPoints()
    #     # self.assertEqual(500, numberOfPoints)
    #     # self.assertEqual(499, steps)
    #
    # def test_simulateOptions_startTime(self):
    #     r = te.loada(self.ant_str)
    #     self.assertRaises(DeprecationWarning, r.setStartTime, 13.5)
    #     self.assertRaises(DeprecationWarning, r.getStartTime)
    #     # r.setStartTime(13.5)
    #     # start = r.getStartTime()
    #     # self.assertAlmostEqual(13.5, start)
    #
    # def test_simulateOptions_endTime(self):
    #     r = te.loada(self.ant_str)
    #     self.assertRaises(DeprecationWarning, r.setEndTime, 200.0)
    #     self.assertRaises(DeprecationWarning, r.getEndTime)
    #     # r.setEndTime(200.0)
    #     # end = r.getEndTime()
    #     # self.assertAlmostEqual(200.0, end)

    # ---------------------------------------------------------------------
    # Jarnac compatibility layer
    # ---------------------------------------------------------------------
    def test_jarnac_fjac(self):
        r = te.loada(self.ant_str)
        m1 = r.fjac()
        m2 = r.getFullJacobian()
        self.assertTrue(np.allclose(m1, m2))

    def test_jarnac_sm(self):
        r = te.loada(self.ant_str)
        m1 = r.sm()
        m2 = r.getFullStoichiometryMatrix()
        self.assertTrue(np.allclose(m1, m2))

    def test_jarnac_fs(self):
        r = te.loada(self.ant_str)
        m1 = r.fs()
        m2 = r.model.getFloatingSpeciesIds()
        self.assertEqual(m1, m2)

    def test_jarnac_bs(self):
        r = te.loada(self.ant_str)
        m1 = r.bs()
        m2 = r.model.getBoundarySpeciesIds()
        self.assertTrue(np.allclose(m1, m2))

    def test_jarnac_rs(self):
        r = te.loada(self.ant_str)
        m1 = r.rs()
        m2 = r.model.getReactionIds()
        self.assertEqual(m1, m2)

    def test_jarnac_ps(self):
        r = te.loada(self.ant_str)
        m1 = r.ps()
        m2 = r.model.getGlobalParameterIds()
        self.assertEqual(m1, m2)

    def test_jarnac_vs(self):
        r = te.loada(self.ant_str)
        m1 = r.vs()
        m2 = r.model.getCompartmentIds()
        self.assertEqual(m1, m2)

    def test_jarnac_dv(self):
        r = te.loada(self.ant_str)
        m1 = r.dv()
        m2 = r.model.getStateVectorRate()
        self.assertTrue(np.allclose(m1, m2))

    def test_jarnac_rv(self):
        r = te.loada(self.ant_str)
        m1 = r.rv()
        m2 = r.model.getReactionRates()
        self.assertTrue(np.allclose(m1, m2))

    def test_jarnac_sv(self):
        r = te.loada(self.ant_str)
        m1 = r.sv()
        m2 = r.model.getFloatingSpeciesConcentrations()
        self.assertTrue(np.allclose(m1, m2))

    # ---------------------------------------------------------------------
    # Stochastic Simulation Methods
    # ---------------------------------------------------------------------
    def test_seed(self):
        r = te.loada('''
        S1 -> S2; k1*S1; k1 = 0.1; S1 = 40
        ''')

        # Simulate from time zero to 40 time units
        result = r.gillespie(0, 40)

        # Simulate on a grid with 10 points from start 0 to end time 40
        result = r.gillespie(0, 40, 10)

        # Simulate from time zero to 40 time units using the given selection list
        # This means that the first column will be time and the second column species S1
        result = r.gillespie(0, 40, ['time', 'S1'])

        # Simulate from time zero to 40 time units, on a grid with 20 points
        # using the give selection list
        result = r.gillespie(0, 40, 20, ['time', 'S1'])

    # ---------------------------------------------------------------------
    # Roadrunner tests
    # ---------------------------------------------------------------------
    def test_roadrunner(self):
        # load test model as SBML
        sbml = te.getTestModel('feedback.xml')
        rr = te.loadSBMLModel(sbml)
        # simulate
        s = rr.simulate(0, 100.0, 200)
        rr.plot(s)

        self.assertIsNotNone(rr)
        self.assertIsNotNone(s)
        self.assertEqual(s.shape[0], 200)
        self.assertEqual(s["time"][0], 0)
        self.assertAlmostEqual(s["time"][-1], 100.0)

    def test_roadrunner_tests(self):
        """ Run the roadrunner tests. """
        import roadrunner.testing
        Nfailed = roadrunner.testing.runTester()
        self.assertEqual(Nfailed, 0)

    def test_loada(self):
        rr = te.loada('''
            model example0
              S1 -> S2; k1*S1
              S1 = 10
              S2 = 0
              k1 = 0.1
            end
        ''')
        self.assertIsNotNone(rr.getModel())

    def test_README_example(self):
        """ Tests the source example in the main README.md. """
        import tellurium as te
        rr = te.loada('''
            model example0
              S1 -> S2; k1*S1
              S1 = 10
              S2 = 0
              k1 = 0.1
            end
        ''')
        result = rr.simulate(0, 40, 500)
        te.plotArray(result)

    def test_complex_simulation(self):
        """ Test complex simulation. """
        model = '''
        model feedback()
           // Reactions:
           J0: $X0 -> S1; (VM1 * (X0 - S1/Keq1))/(1 + X0 + S1 + S4^h);
           J1: S1 -> S2; (10 * S1 - 2 * S2) / (1 + S1 + S2);
           J2: S2 -> S3; (10 * S2 - 2 * S3) / (1 + S2 + S3);
           J3: S3 -> S4; (10 * S3 - 2 * S4) / (1 + S3 + S4);
           J4: S4 -> $X1; (V4 * S4) / (KS4 + S4);

          // Species initializations:
          S1 = 0; S2 = 0; S3 = 0;
          S4 = 0; X0 = 10; X1 = 0;

          // Variable initialization:
          VM1 = 10; Keq1 = 10; h = 10; V4 = 2.5; KS4 = 0.5;
        end
        '''
        r = te.loada(model)
        result = r.simulate(0, 40, 101)
        r.plotWithLegend(result)

    def test_getTelluriumVersionInfo(self):
        version = te.getTelluriumVersion()
        self.assertTrue(isinstance(version, str))
        self.assertTrue(len(version) > 0)
        self.assertEqual(version, te.__version__)


if __name__ == '__main__':
    unittest.main()
