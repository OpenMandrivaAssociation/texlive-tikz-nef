Name:		texlive-tikz-nef
Version:	55920
Release:	2
Summary:	Create diagrams for neural networks constructed with the methods of the Neural Engineering Framework (NEF)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikz-nef
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-nef.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-nef.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The nef TikZ library provides predefined styles and shapes to
create diagrams for neural networks constructed with the
methods of the Neural Engineering Framework (NEF). The
following styles are supported: ea: ensemble array ens:
ensemble ext: external input or output inhibt: inhibitory
connection net: network pnode: pass-through node rect:
rectification ensemble recurrent: recurrent connection

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikz-nef
%doc %{_texmfdistdir}/doc/latex/tikz-nef

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
