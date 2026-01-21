HED Test Suite
==============

.. sidebar:: Quick links
   
   * `HED homepage <https://www.hedtags.org/>`_ 

   * `HED specification <https://www.hedtags.org/hed-specification>`_ 

   * `Python validator <https://github.com/hed-standard/hed-python>`_

   * `JavaScript validator <https://github.com/hed-standard/hed-javascript>`_

   * `HED schemas <https://github.com/hed-standard/hed-schemas>`_

   * `HED organization <https://github.com/hed-standard/>`_  

Welcome to the HED Test Suite documentation! This repository provides the **official JSON test cases** for validating HED (Hierarchical Event Descriptors) validator implementations across all platforms.

What is the HED Test Suite?
----------------------------

The HED Test Suite is a centralized, version-controlled collection of JSON test cases that ensure consistent validation behavior across all HED validator implementations. Tests are designed to:

* **Validate validators**: Ensure Python, JavaScript, and future implementations produce consistent results
* **Specify behavior**: Provide machine-readable examples of HED validation rules  
* **Enable AI training**: Include structured explanations and correction examples for AI systems
* **Prevent regressions**: Catch validation changes across versions

Key Features
------------

* **Comprehensive coverage**: 136 test cases covering 33 error codes
* **Multiple test types**: String, sidecar, event, and combo tests
* **AI-friendly**: 100% of tests include explanations and correction strategies
* **Cross-platform**: Single source of truth for all validator implementations
* **Automated validation**: JSON schema validation ensures test quality

Getting Started
---------------

.. toctree::
   :maxdepth: 2

   Introduction <introduction>
   Validator Integration Guide <validator_integration>

Test Suite Documentation
-------------------------

.. toctree::
   :maxdepth: 2

   Test Format Specification <test_format>
   Test Coverage Report <test_coverage>
   Test Index <test_index>
   Contributing Tests <../CONTRIBUTING>

For Validator Developers
-------------------------

If you're building or maintaining a HED validator, the test suite provides comprehensive test cases to ensure your implementation matches the specification. See the :doc:`validator_integration` guide for details on consuming these tests.

For Contributors
----------------

Want to add new test cases or improve existing ones? See our :doc:`../CONTRIBUTING` guide for guidelines on test file format, naming conventions, and the contribution process.

Repository
----------

* **Source**: https://github.com/hed-standard/hed-tests
* **Issues**: https://github.com/hed-standard/hed-tests/issues
* **License**: MIT

   User guide <user_guide>

API documentation
-----------------

.. toctree::
   :maxdepth: 2

   API reference <api/index>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
