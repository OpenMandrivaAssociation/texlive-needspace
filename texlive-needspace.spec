%global tl_name needspace
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3e
Release:	%{tl_revision}.1
Summary:	Insert pagebreak if not enough space
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/needspace
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/needspace.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/needspace.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/needspace.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides commands to disable pagebreaking within a given vertical space.
If there is not enough space between the command and the bottom of the
page, a new page will be started.

