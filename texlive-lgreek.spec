# revision 21818
# category Package
# catalog-ctan /macros/latex/contrib/lgreek
# catalog-date 2011-03-14 20:27:38 +0100
# catalog-license gpl2
# catalog-version undef
Name:		texlive-lgreek
Version:	20110314
Release:	1
Summary:	LaTeX macros for using Silvio Levy's Greek fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lgreek
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lgreek.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lgreek.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A conversion of Silvio Levy's Plain TeX macros for use with
LaTeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
