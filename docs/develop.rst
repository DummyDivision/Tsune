.. _Setting up a development environment:

Setting up a development environment
====================================

This guide will help you set up a working development environment for
Tsune


Requirements
------------

1. A `working and configured`_ Git (`download`_)
2. VirtualBox `compatible`_ with Vagrant
   (`download <https://www.virtualbox.org/wiki/Download_Old_Builds_4_2>`__)
3. Vagrant (`download <http://downloads.vagrantup.com/>`__)
4. PyCharm Professional
   (`download <http://www.jetbrains.com/pycharm/download/index.html>`__)
5. VirtualBox installation folder in PATH environment variable

.. _Setting up Vagrant:

Setting up Vagrant
------------------

1. Open PyCharm
2. Select *Open from Version Control*
3. Select either *Github* or *Git* and input the repository information
4. When asked whether PyCharm should open the project for you, select
   *Yes*
5. Select *Tools* > *Vagrant* > *Up* and wait for Vagrant to finish.
   This will take a long time (~30min), so grab a coffee or get some
   sleep. When it's finished, you will see *Process finished with exit
   code 0*

.. _Setting up the remote python interpreter:

Setting up the remote python interpreter
----------------------------------------

2. Select *File > Settings* and click on *Project Interpreter >
   Configure Interpreters*
3. Click the *+* button on the right and select *Remote...*
4. Click *Fill from vagrant config* and *Ok*
5. Click *Test Connection*. Answer the authenticity warning with *Yes*
   and click *Ok*
6. Click *Ok* to close the interpreter setup and wait for the process to
   finish. This may take a few moments
7. When asked whether you want to set the interpreter as Project
   Interpreter, select *Yes*
8. Click *Ok* to close the settings window

.. _Configure Django integration:

Configure Django integration
----------------------------

1. Select *File > Settings* and click on *Django Support*. Make sure
   that *Enable Django Support* is ticked
2. Click the *...* button next to *Settings*. Select
   *tsune/settings.py*. Click *Ok*
3. Close the Settings window with *Ok*
4. Click *Run > Edit Configurations*
5. If *Django server* has an entry named *tsune*, select the entry and
   continue with step 7
6. Click the *+* button. Select *Django server*
7. Configure everything **exactly** as follows:
    **Name**: *tsune*
    **Host**: *0.0.0.0*
    **Port**: *8000*
    **Run Browser**: *http://127.0.0.1:8080*
8. Close the Run configurations dialog by clicking *Ok*

.. _working and configured: https://help.github.com/articles/set-up-git
.. _download: http://git-scm.com/download/win
.. _compatible: http://docs.vagrantup.com/v2/virtualbox/index.html