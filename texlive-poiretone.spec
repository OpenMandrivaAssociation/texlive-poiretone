%global tl_name poiretone
%global tl_revision 78931

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	PoiretOne family of fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/poiretone
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/poiretone.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/poiretone.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the PoiretOne family of fonts, designed by Denis Masharov. PoiretOne is
a decorative geometric grotesque with a hint of Art Deco and
constructivism. There is currently just a regular weight and an
artificially emboldened bold.

