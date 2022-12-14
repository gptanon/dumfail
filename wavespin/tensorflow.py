# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2022- John Muradeli
#
# Distributed under the terms of the MIT License
# (see wavespin/__init__.py for details)
# -----------------------------------------------------------------------------
from .scattering1d.frontend.tensorflow_frontend import (
    ScatteringTensorFlow1D as Scattering1D,
    TimeFrequencyScatteringTensorFlow1D as TimeFrequencyScattering1D)

Scattering1D.__module__ = 'wavespin.tensorflow'
Scattering1D.__name__ = 'Scattering1D'

TimeFrequencyScattering1D.__module__ = 'wavespin.tensorflow'
TimeFrequencyScattering1D.__name__ = 'TimeFrequencyScattering1D'

__all__ = ['Scattering1D', 'TimeFrequencyScattering1D']
