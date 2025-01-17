# Copyright (c) SenseTime. All Rights Reserved.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from pysot.core.config import cfg
from pysot.tracker.siamrpn_tracker import SiamRPNTracker
from pysot.tracker.siammask_tracker import SiamMaskTracker
from pysot.tracker.siamrpnlt_tracker import SiamRPNLTTracker
from pysot.tracker.siammask_e_tracker import SiamMaskETracker
from pysot.tracker.siammask_axis_aligned_tracker import SiamMaskAATracker
from pysot.tracker.siammask_e_axis_aligned_tracker import SiamMaskEAATracker

TRACKS = {
          'SiamRPNTracker': SiamRPNTracker,
          'SiamMaskTracker': SiamMaskTracker,
          'SiamRPNLTTracker': SiamRPNLTTracker,
          'SiamMaskETracker': SiamMaskETracker,
          'SiamMaskAATracker': SiamMaskAATracker,
          'SiamMaskEAATracker': SiamMaskEAATracker
         }


def build_tracker(model):
    return TRACKS[cfg.TRACK.TYPE](model)
