Name:		texlive-substr
Version:	16117
Release:	2
Summary:	Deal with substrings in strings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/substr
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/substr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/substr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The substr package provides commands to deal with substrings of
strings. Macros are provided to: - determine if one string is a
substring of another, - return the parts of a string before or
after a substring and - count the number of occurrences of a
substring.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/substr/substr.sty
%doc %{_texmfdistdir}/doc/latex/substr/ChangeLog
%doc %{_texmfdistdir}/doc/latex/substr/README
%doc %{_texmfdistdir}/doc/latex/substr/testsubstr.pdf
%doc %{_texmfdistdir}/doc/latex/substr/testsubstr.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
