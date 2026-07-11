%global tl_name substr
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Deal with substrings in strings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/substr
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/substr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/substr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands to deal with substrings of strings. Macros
are provided to: determine if one string is a substring of another,
return the parts of a string before or after a substring, and count the
number of occurrences of a substring.

