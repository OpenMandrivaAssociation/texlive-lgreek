# revision 21818
# category Package
# catalog-ctan /macros/latex/contrib/lgreek
# catalog-date 2011-03-14 20:27:38 +0100
# catalog-license gpl2
# catalog-version undef
Name:		texlive-lgreek
Version:	20110314
Release:	10
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110314-2
+ Revision: 753299
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110314-1
+ Revision: 718851
- texlive-lgreek
- texlive-lgreek
- texlive-lgreek
- texlive-lgreek

