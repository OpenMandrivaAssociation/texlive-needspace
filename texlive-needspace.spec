Name:		texlive-needspace
Version:	29601
Release:	2
Summary:	Insert pagebreak if not enough space
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/needspace
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/needspace.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/needspace.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/needspace.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
