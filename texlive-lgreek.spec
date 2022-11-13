Name:		texlive-lgreek
Version:	21818
Release:	1
Summary:	LaTeX macros for using Silvio Levy's Greek fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lgreek
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lgreek.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lgreek.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A conversion of Silvio Levy's Plain TeX macros for use with
LaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lgreek/LGcmr.fd
%{_texmfdistdir}/tex/latex/lgreek/LGcmtt.fd
%{_texmfdistdir}/tex/latex/lgreek/LGenc.def
%{_texmfdistdir}/tex/latex/lgreek/lgreek.sty
%doc %{_texmfdistdir}/doc/latex/lgreek/README
%doc %{_texmfdistdir}/doc/latex/lgreek/lgreekuse.pdf
%doc %{_texmfdistdir}/doc/latex/lgreek/lgreekuse.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
