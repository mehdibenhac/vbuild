# -*- coding: utf-8 -*-
import vbuild
import pytest
import sys


@pytest.mark.skipif(not vbuild.hasLess, reason="requires lesscpy")
def test_less():
    h = """<template><div>XXX</div></template>
    <Style scoped Lang = "leSS" >
    body {
        border-width: 2px *3;
    }
    </style>"""
    r = vbuild.VBuild("comp.vue", h)
    assert "6px" in r.style

    h = """<template><div>XXX</div></template>
    <Style scoped lang="less">
    body {
        font: @unknown;
    }
    </style>"""
    r = vbuild.VBuild("comp.vue", h)
    with pytest.raises(
        vbuild.VBuildException
    ):  # vbuild.VBuildException: Component 'comp.vue' got a CSS-PreProcessor trouble : Error evaluating expression:
        r.style
