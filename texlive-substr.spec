# revision 16117
# category Package
# catalog-ctan /macros/latex/contrib/substr
# catalog-date 2009-10-20 22:03:50 +0200
# catalog-license lppl1
# catalog-version 1.2
Name:		texlive-substr
Version:	1.2
Release:	1
Summary:	Deal with substrings in strings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/substr
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/substr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/substr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The substr package provides commands to deal with substrings of
strings. Macros are provided to: - determine if one string is a
substring of another, - return the parts of a string before or
after a substring and - count the number of occurrences of a
substring.

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
%{_texmfdistdir}/tex/latex/substr/substr.sty
%doc %{_texmfdistdir}/doc/latex/substr/ChangeLog
%doc %{_texmfdistdir}/doc/latex/substr/README
%doc %{_texmfdistdir}/doc/latex/substr/testsubstr.pdf
%doc %{_texmfdistdir}/doc/latex/substr/testsubstr.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
