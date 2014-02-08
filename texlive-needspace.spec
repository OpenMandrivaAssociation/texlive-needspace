# revision 19684
# category Package
# catalog-ctan /macros/latex/contrib/needspace
# catalog-date 2010-09-12 11:26:42 +0200
# catalog-license lppl
# catalog-version 1.3c
Name:		texlive-needspace
Version:	1.3c
Release:	3
Summary:	Insert pagebreak if not enough space
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/needspace
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/needspace.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/needspace.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/needspace.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides commands to disable pagebreaking within a given
vertical space. If there is not enough space between the
command and the bottom of the page, a new page will be started.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/needspace/needspace.sty
%doc %{_texmfdistdir}/doc/latex/needspace/README
%doc %{_texmfdistdir}/doc/latex/needspace/needspace.pdf
#- source
%doc %{_texmfdistdir}/source/latex/needspace/needspace.ins
%doc %{_texmfdistdir}/source/latex/needspace/needspace.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3c-2
+ Revision: 754255
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3c-1
+ Revision: 719108
- texlive-needspace
- texlive-needspace
- texlive-needspace
- texlive-needspace

