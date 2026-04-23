from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from anndata import AnnData


def deconvolve(sc_adata: AnnData, st_adata: AnnData) -> AnnData:
    """Estimate cell-type proportions for spatial transcriptomics spots.

    Parameters
    ----------
    sc_adata : AnnData
        Annotated single-cell reference with cell-type labels in ``obs``.
        Used to derive cell-type signatures for deconvolution.
    st_adata : AnnData
        Annotated spatial transcriptomics data. Rows are spots/beads and
        columns are genes shared with ``sc_adata``.

    Returns
    -------
    AnnData
        A copy of ``st_adata`` with estimated cell-type proportions stored
        in ``obsm['proportions']`` (spots x cell types).

    Raises
    ------
    NotImplementedError
        This is a placeholder; the deconvolution algorithm is not yet
        implemented.
    """
    raise NotImplementedError
