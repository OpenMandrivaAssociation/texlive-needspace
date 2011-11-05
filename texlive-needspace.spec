# revision 19684
# category Package
# catalog-ctan /macros/latex/contrib/needspace
# catalog-date 2010-09-12 11:26:42 +0200
# catalog-license lppl
# catalog-version 1.3c
Name:		texlive-needspace
Version:	1.3c
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Provides commands to disable pagebreaking within a given
vertical space. If there is not enough space between the
command and the bottom of the page, a new page will be started.

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
%{_texmfdistdir}/tex/latex/needspace/needspace.sty
%doc %{_texmfdistdir}/doc/latex/needspace/README
%doc %{_texmfdistdir}/doc/latex/needspace/needspace.pdf
#- source
%doc %{_texmfdistdir}/source/latex/needspace/needspace.ins
%doc %{_texmfdistdir}/source/latex/needspace/needspace.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
