# revision 16117
# category Package
# catalog-ctan /macros/latex/contrib/substr
# catalog-date 2009-10-20 22:03:50 +0200
# catalog-license lppl1
# catalog-version 1.2
Name:		texlive-substr
Version:	1.2
Release:	2
Summary:	Deal with substrings in strings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/substr
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/substr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/substr.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 756309
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 719607
- texlive-substr
- texlive-substr
- texlive-substr
- texlive-substr

