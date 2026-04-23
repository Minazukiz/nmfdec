from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from anndata import AnnData


def deconvolve(sc_adata: AnnData, st_adata: AnnData) -> AnnData:
    raise NotImplementedError
