# revision 29601
# category Package
# catalog-ctan /macros/latex/contrib/needspace
# catalog-date 2013-04-01 14:35:12 +0200
# catalog-license lppl
# catalog-version 1.3d
Name:		texlive-needspace
Version:	1.3d
Release:	2
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
