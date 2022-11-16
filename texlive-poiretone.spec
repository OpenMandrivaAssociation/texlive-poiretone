Name:		texlive-poiretone
Version:	64856
Release:	1
Summary:	PoiretOne family of fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/poiretone
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poiretone.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poiretone.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the PoiretOne family of fonts, designed by Denis
Masharov. PoiretOne is a decorative geometric grotesque with a
hint of Art Deco and constructivism. There is currently just a
regular weight and an artificially emboldened bold.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/poiretone
%{_texmfdistdir}/fonts/vf/public/poiretone
%{_texmfdistdir}/fonts/type1/public/poiretone
%{_texmfdistdir}/fonts/truetype/public/poiretone
%{_texmfdistdir}/fonts/tfm/public/poiretone
%{_texmfdistdir}/fonts/map/dvips/poiretone
%{_texmfdistdir}/fonts/enc/dvips/poiretone
%doc %{_texmfdistdir}/doc/fonts/poiretone

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
