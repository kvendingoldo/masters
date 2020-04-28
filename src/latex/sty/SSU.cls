\LoadClass{article}
\RequirePackage[14pt]{extsizes}
\RequirePackage[
  		a4paper, mag=1000,
  		left=2.5cm, right=1.5cm, top=2cm, bottom=2cm, bindingoffset=0cm,
		headheight=0cm, footskip=1cm, headsep=0cm
	]{geometry}
\RequirePackage{setspace}
\RequirePackage{calc}
\RequirePackage{titlesec}
\RequirePackage{titletoc}
\RequirePackage{caption}




% --------------------------------------------------------------------------%
% Input data
% --------------------------------------------------------------------------%
\def\chair#1{\gdef\@chair{#1}}\chair{}
\def\worktype#1{\gdef\@worktype{#1}}
\def\typework#1{\gdef\@typework{#1}}
\def\worktitle#1{\gdef\@worktitle{#1}}
\def\course#1{\gdef\@course{#1}}
\def\group#1{\gdef\@group{#1}}
\def\department#1{\gdef\@department{#1}}\department{\cyr\cyrf\cyra\cyrk%
\cyru\cyrl\cyrsftsn\cyrt\cyre\cyrt\cyra}
\def\otdelenie#1{\gdef\@otdelenie{#1}}
\def\studentName#1{\gdef\@studentName{#1}}
\def\satitle#1{\gdef\@satitle{#1}}
\def\saname#1{\gdef\@saname{#1}}
\def\chtitle#1{\gdef\@chtitle{#1}}
\def\chname#1{\gdef\@chname{#1}}
\def\year#1{\gdef\@year{#1}}
\def\spectype#1{\gdef\@spectype{#1}}
\def\workform#1{\gdef\@workform{#1}}
\def\practtype#1{\gdef\@practtype{#1}}\practtype{\cyr\cyru\cyrch\cyre\cyrb%
\cyrn\cyra\cyrya}
\def\term#1{\gdef\@term{#1}}\term{2}
\def\duration#1{\gdef\@duration{#1}}\duration{0}
\def\practStart#1{\gdef\@practStart{#1}}\practStart{01.01.2012}
\def\practFinish#1{\gdef\@practFinish{#1}}\practFinish{01.01.2012}

\def\patitle#1{\gdef\@patitle{#1}}\patitle{\@satitle}
\def\paname#1{\gdef\@paname{#1}}\paname{\@saname}

\def\napravlenie#1{\gdef\@napravlenie{#1}}\napravlenie{}

\def\studenttitle#1{\gdef\@studenttitle{#1}}\studenttitle{\cyr\cyrs\cyrt%
\cyru\cyrd\cyre\cyrn\cyrt\cyra}


\newcommand{\MakeTitle}{}

\def\workname#1{\gdef\@workname{#1}}


% --------------------------------------------------------------------------%

\DeclareOption{times}{%
    \renewcommand{\rmdefault}{ftm}
}

\DeclareOption{spec}{%
    \spectype{\cyr\cyrs\cyrp\cyre\cyrc\cyri\cyra\cyrl\cyrsftsn\cyrn\cyro%
    \cyrs\cyrt\cyri}
    \workform{\cyr\CYRS\CYRP\CYRE\CYRC\CYRI\CYRA\CYRL\CYRI\CYRS\CYRT\CYRA}
}

\DeclareOption{bachelor}{%
    \spectype{\cyr\cyrn\cyra\cyrp\cyrr\cyra\cyrv\cyrl\cyre\cyrn\cyri\cyrya}
    \workform{\cyr\CYRB\CYRA\CYRK\CYRA\CYRL\CYRA\CYRV\CYRR\CYRA}
}

\DeclareOption{master}{%
    \spectype{\cyr\cyrn\cyra\cyrp\cyrr\cyra\cyrv\cyrl\cyre\cyrn\cyri\cyrya}
    \workform{\cyr\CYRM\CYRA\CYRG\CYRI\CYRS\CYRT\CYRR\CYRA}
}

\DeclareOption{coursework}{%
    \worktype{\cyr\CYRK\cyru\cyrr\cyrs\cyro\cyrv\cyra\cyrya\ \cyrr\cyra\cyrb%
    \cyro\cyrt\cyra}
    \renewcommand{\MakeTitle}{\CDMakeTitle}
    \workname{\MakeUppercase{\@worktype}}
    \typework{\cyr\cyrn\cyra\cyrp\cyri\cyrs\cyra\cyrn\cyra}
}

\DeclareOption{diploma}{%
    \worktype{\cyr\CYRV\cyrery\cyrp\cyru\cyrs\cyrk\cyrn\cyra\cyrya\ \cyrk\cyrv%
    \cyra\cyrl\cyri\cyrf\cyri\cyrk\cyra\cyrc\cyri\cyro\cyrn\cyrn\cyra%
    \cyrya\ \cyrr\cyra\cyrb\cyro\cyrt\cyra}
    \renewcommand{\MakeTitle}{\CDMakeTitle}
    \workname{\MakeUppercase{\@worktype}\ \@workform}
    \typework{\cyr\cyrn\cyra\cyrp\cyri\cyrs\cyra\cyrn\cyra}
}

\DeclareOption{pract}{%
    \worktype{\cyr\CYRO\cyrt\cyrch\cyre\cyrt\ \cyro\ \cyrp\cyrr\cyra\cyrk\cyrt%
    \cyri\cyrk\cyre}
    \renewcommand{\MakeTitle}{\MakeTitlePr}
    \typework{\cyr\cyrn\cyra\cyrp\cyri\cyrs\cyra\cyrn}
}

\DeclareOption{referat}{%
    \worktype{\cyr\CYRR\cyre\cyrf\cyre\cyrr\cyra\cyrt}
    \workname{\MakeUppercase{\@worktype}}
    \renewcommand{\MakeTitle}{\RefMakeTitle}
    \typework{\cyr\cyrn\cyra\cyrp\cyri\cyrs\cyra\cyrn}
}

\DeclareOption{och}{%
    \otdelenie{\cyr\cyro\cyrch\cyrn\cyro\cyrishrt\ \cyrf\cyro\cyrr\cyrm%
    \cyrery\ \cyro\cyrb\cyru\cyrch\cyre\cyrn\cyri\cyrya}
}

\DeclareOption{zaoch}{%
   \otdelenie{\cyr\cyrz\cyra\cyro\cyrch\cyrn\cyro\cyrishrt\ \cyrf\cyro\cyrr%
   \cyrm\cyrery\ \cyro\cyrb\cyru\cyrch\cyre\cyrn\cyri\cyrya}
}

\ExecuteOptions{coursework,och,bachelor}
\ProcessOptions

% --------------------------------------------------------------------------%
\newcommand*{\hm}[1]{#1\nobreak\discretionary{}%
{\hbox{$\mathsurround=0pt #1$}}{}}
% --------------------------------------------------------------------------%

% --------------------------------------------------------------------------%

\onehalfspacing
\parindent=1.25cm
\pagestyle{headings}
\renewcommand{\@oddhead}{}
\renewcommand{\@oddfoot}{\hfil \thepage}

% --------------------------------------------------------------------------%
% Table and figure numbering by sections
% --------------------------------------------------------------------------%
\newcommand{\secNumbering}{
    \renewcommand{\thefigure}{\arabic{section}.\arabic{figure}}
    \renewcommand{\thetable}{\arabic{section}.\arabic{table}}
    \renewcommand{\theequation}{\arabic{section}.\arabic{equation}}
    \@addtoreset{figure}{section}
    \@addtoreset{table}{section}
    \@addtoreset{equation}{section}
}
% --------------------------------------------------------------------------%

% --------------------------------------------------------------------------%
% Table and figure captions
% --------------------------------------------------------------------------%
\def\CaptionName#1{\gdef\@captionname{#1}}
\newlength\tmp %10cm
\setlength{\tmp}{1ex}
\setlength{\belowcaptionskip}{1ex}
\setlength{\abovecaptionskip}{1ex}

\captionsetup[figure]{name=\CYRR\cyri\cyrs\cyru\cyrn\cyro\cyrk, labelsep=endash,
                justification=centering, font={small}, skip=\abovecaptionskip, position=below}
\captionsetup[table]{name=\CYRT\cyra\cyrb\cyrl\cyri\cyrc\cyra, labelsep=endash, format=plain,
                justification=RaggedRight, singlelinecheck=false, font={small}, position=top}

% --------------------------------------------------------------------------%
% Table of contents
% --------------------------------------------------------------------------%
\renewcommand{\tableofcontents}%
{\structformat\section*{\uppercase{\cyr\CYRS\CYRO\CYRD\CYRE\CYRR\CYRZH\CYRA%
\CYRN\CYRI\CYRE}}\@starttoc{toc}
\thispagestyle{empty}}

\renewcommand{\@dotsep}{1.5}
\renewcommand{\@pnumwidth}{1.0em}

\newcommand{\l@abcd}[2]{{\@dottedtocline{0}{0pt}{0pt}{#1}{#2}}}

\renewcommand{\l@section}{\@dottedtocline{1}{0em}{1.5em}}
\renewcommand{\l@subsection}{\@dottedtocline{2}{1.5em}{2.3em}}
% --------------------------------------------------------------------------%

% --------------------------------------------------------------------------%
% Sections, subsections
% --------------------------------------------------------------------------%
% Numbering
\renewcommand{\thesection}{\arabic{section} }
\renewcommand{\thesubsection}{\arabic{section}.\arabic{subsection} }
\renewcommand{\thesubsubsection}{\arabic{section}.\arabic{subsection}.\arabic{subsubsection} }

\newcommand{\sectionbreak}{\clearpage}

% Contents, intro, conclusion
\newcommand{\structformat}
{
   \titleformat{\section}[block]
   {\centering\bfseries}
   {\thesection }{}{}
}

% Sections, subsections
\newcommand{\secformat}
{
    \titleformat{\section}[block]
    {\hspace{1.25cm}\raggedright\bfseries}
    {\thesection}{1ex}{}
}

\newcommand{\starsection}[1]{
    \structformat
    \section*{#1}
    \addcontentsline{toc}{section}{#1}
    \setcounter{section}{0}
    \secformat
}

\newcommand{\intro}{\starsection{\cyr\CYRV\CYRV\CYRE\CYRD\CYRE%
\CYRN\CYRI\CYRE}}
\newcommand{\abbreviations}{\starsection{\CYRO\CYRB\CYRO\CYRZ\CYRN\CYRA%
\CYRCH\CYRE\CYRN\CYRI\CYRYA\ \CYRI\ \CYRS\CYRO\CYRK\CYRR\CYRA\CYRSHCH%
\CYRE\CYRN\CYRI\CYRYA}}
\newcommand{\definitions}{\starsection{\CYRO\CYRP\CYRR\CYRE\CYRD\CYRE%
\CYRL\CYRE\CYRN\CYRI\CYRYA}}
\newcommand{\defabbr}{\starsection{\CYRO\CYRP\CYRR\CYRE\CYRD\CYRE\CYRL%
\CYRE\CYRN\CYRI\CYRYA, \CYRO\CYRB\CYRO\CYRZ\CYRN\CYRA\CYRCH\CYRE\CYRN%
\CYRI\CYRYA\ \CYRI\ \CYRS\CYRO\CYRK\CYRR\CYRA\CYRSHCH\CYRE\CYRN\CYRI\CYRYA}}
\newcommand{\conclusion}{\starsection{\cyr\CYRZ\CYRA\CYRK\CYRL\CYRYU%
\CYRCH\CYRE\CYRN\CYRI\CYRE}}

% Section and subsection parameters
\titlespacing{\section}
{0cm}{3ex plus 1ex minus .2ex}{3ex plus.2ex}

\titleformat{\subsection}[block]
{\hspace{1.25cm}\normalfont\bfseries}
{\thesubsection}{1ex}{}
\titlespacing{\subsection}
{0cm}{2ex plus 1ex minus .2ex}{.3ex plus.2ex}

\titleformat{\subsubsection}[block]
{\hspace{1.25cm}\normalfont}
{\thesubsubsection}{1ex}{}
\titlespacing{\subsubsection}
{0cm}{2ex plus 1ex minus .2ex}{.3ex plus.2ex}

% --------------------------------------------------------------------------%

% --------------------------------------------------------------------------%




\makeatletter
\def\redeflsection{\def\l@section{\@dottedtocline{1}{0em}{10em}}}
\renewcommand{\appendix}{\par%

    \renewcommand{\secNumbering}{
    \renewcommand{\thefigure}{\Asbuk{section}.\arabic{figure}}
    \renewcommand{\thetable}{\Asbuk{section}.\arabic{table}}
    \renewcommand{\theequation}{\Asbuk{section}.\arabic{equation}}
    \@addtoreset{figure}{section}
    \@addtoreset{table}{section}
    \@addtoreset{equation}{section}
}




  %\secNumbering
  \setcounter{section}{0}%
  \setcounter{subsection}{0}%
  \renewcommand{\appendixname}{\cyr\CYRP\CYRR\CYRI\CYRL\CYRO\CYRZH\CYRE%
  \CYRN\CYRI\CYRE}%
  \def\sectionname{\appendixname}%
  \addtocontents{toc}{\protect\redeflsection}%
  \gdef\thesection{\@Asbuk\c@section}%

  \titleformat{\section}[display]
    {\centering\normalfont\bfseries}
  {\appendixname\hspace{1ex}\thesection}{1ex}{}
  \titlespacing{\section}
  {0cm}{1ex plus 01ex minus .2ex}{4ex plus.2ex}

  \titlecontents{section}
  [3ex]
  {\hspace{-3ex}}
  {\appendixname~\thecontentslabel\hspace{2ex}}
  {\hspace{2.3em}}
  {\titlerule*[0.98ex]{.}\contentspage}

}


% --------------------------------------------------------------------------%


\newcommand{\signature}[2]{
\hbox to 7cm{#1\hfill} \hbox to 3cm{\hrulefill} \hbox to 6cm{\hfill #2}}

% --------------------------------------------------------------------------%
% Title pages
% --------------------------------------------------------------------------%
\newcommand{\shapka}{{\centering \CYRM\cyri\cyrn\cyri\cyrs\cyrt\cyre%
\cyrr\cyrs\cyrt\cyrv\cyro\ \cyro\cyrb\cyrr\cyra\cyrz\cyro\cyrv\cyra%
\cyrn\cyri\cyrya\ \cyri\ \cyrn\cyra\cyru\cyrk\cyri\ \CYRR\cyro\cyrs\cyrs%
\cyri\cyrishrt\cyrs\cyrk\cyro\cyrishrt\ \CYRF\cyre\cyrd\cyre\cyrr\cyra%
\cyrc\cyri\cyri\\[14pt]
\CYRF\CYRE\CYRD\CYRE\CYRR\CYRA\CYRL\CYRSFTSN\CYRN\CYRO\CYRE\ % federalnoe
\CYRG\CYRO\CYRS\CYRU\CYRD\CYRA\CYRR\CYRS\CYRT\CYRV\CYRE\CYRN\CYRN\CYRO\CYRE\ % gossudarstvennoe
\CYRB\CYRYU\CYRD\CYRZH\CYRE\CYRT\CYRN\CYRO\CYRE\ % budjetnoe
\CYRO\CYRB\CYRR\CYRA\CYRZ\CYRO\CYRV\CYRA\CYRT\CYRE\CYRL\CYRSFTSN\CYRN\CYRO\CYRE\ % obrazovatelnoe
\CYRU\CYRCH\CYRR\CYRE\CYRZH\CYRD\CYRE\CYRN\CYRI\CYRE\\ % uchrejdenie
\CYRV\CYRERY\CYRS\CYRSH\CYRE\CYRG\CYRO\ % vishego
%\CYRP\CYRR\CYRO\CYRF\CYRE\CYRS\CYRS\CYRI\CYRO\CYRN\CYRA\CYRL\CYRSFTSN\CYRN\CYRO\CYRG\CYRO\ % professionalnogo
\CYRO\CYRB\CYRR\CYRA\CYRZ\CYRO\CYRV\CYRA\CYRN\CYRI\CYRYA\\ % obrazovania
<<\CYRS\CYRA\CYRR\CYRA\CYRT\CYRO\CYRV\CYRS\CYRK\CYRI\CYRISHRT\ \CYRN\CYRA\CYRC\CYRI\CYRO\CYRN\CYRA\CYRL\CYRSFTSN\CYRN\CYRERY\CYRISHRT \
\CYRI\CYRS\CYRS\CYRL\CYRE\CYRD\CYRO\CYRV\CYRA\CYRT\CYRE\CYRL\CYRSFTSN\CYRS\CYRK\CYRI\CYRISHRT\
% saratovskii %\CYRN\CYRA\CYRU\CYRCH\CYRN\CYRO- 
\CYRG\CYRO\CYRS\CYRU\CYRD\CYRA\CYRR\CYRS\CYRT\CYRV\CYRE\CYRN\CYRN\CYRERY\CYRISHRT\ % gosudarstvennii
\CYRU\CYRN\CYRI\CYRV\CYRE\CYRR\CYRS\CYRI\CYRT\CYRE\CYRT\\ % universitet
\CYRI\CYRM\CYRE\CYRN\CYRI\ \CYRN.\CYRG. \CYRCH\CYRE\CYRR\CYRN\CYRERY%
\CYRSH\CYRE\CYRV\CYRS\CYRK\CYRO\CYRG\CYRO>>\vspace{14pt}\\}}

\newcommand{\CDMakeTitle}
{
\thispagestyle{empty}
\shapka

\vspace{0.5cm}
\begin{flushleft}
\parbox{8cm}{
\raggedright
\CYRK\cyra\cyrf\cyre\cyrd\cyrr\cyra\ \@chair
}

% chair

\end{flushleft}

\vspace{1cm}
{\centering
\textbf{\MakeUppercase{\@worktitle}}
\\[0.3cm]
{\@workname}

}

\vspace{1.5cm}
\begin{flushleft}
\@studenttitle\ \@course\ \cyrk\cyru\cyrr\cyrs\cyra\ \@group\ \cyrg%
\cyrr\cyru\cyrp\cyrp\cyrery\\
\@spectype\ \@napravlenie\\
\@department\\
\@studentName
\end{flushleft}
\vfill

\noindent
\CYRN\cyra\cyru\cyrch\cyrn\cyrery\cyrishrt\ \cyrr\cyru\cyrk\cyro\cyrv%
\cyro\cyrd\cyri\cyrt\cyre\cyrl\cyrsftsn\\
\signature{\@satitle}{\@saname}\\[14pt]
\CYRZ\cyra\cyrv\cyre\cyrd\cyru\cyryu\cyrshch\cyri\cyrishrt\ \cyrk\cyra%
\cyrf\cyre\cyrd\cyrr\cyro\cyrishrt\\
\signature{\@chtitle}{\@chname}

\vfill
{\centering{\cyr\CYRS\cyra\cyrr\cyra\cyrt\cyro\cyrv\ \@year}

}
\newpage
}
% --------------------------------------------------------------------------%

% --------------------------------------------------------------------------%
% Title page of internship
% --------------------------------------------------------------------------%
\newcommand{\MakeTitlePr}
{
\thispagestyle{empty}
\begin{center}
\shapka
\end{center}
\vspace{0.5cm}


\begin{flushright}
  \parbox{7cm}{
    \begin{flushleft}
    \CYRU\CYRT\CYRV\CYRE\CYRR\CYRZH\CYRD\CYRA\CYRYU\\
    \CYRZ\cyra\cyrv.\cyrk\cyra\cyrf\cyre\cyrd\cyrr\cyro\cyrishrt,\\
    \@chtitle\\
    \hbox to 7cm{\hrulefill\ \@chname}
    \end{flushleft}
  }
\end{flushright}

\vspace{1cm}
\begin{center}\textbf{\MakeUppercase{\@worktype}}\end{center}
\begin{flushleft}
    \vspace{12pt}
    \@studenttitle\ \@course\ \cyrk\cyru\cyrr\cyrs\cyra\ \@group\ \cyrg%
    \cyrr\cyru\cyrp\cyrp\cyrery\ \@department\\
    \@studentName
\vspace{0.5cm}


    \cyrv\cyri\cyrd\ \cyrp\cyrr\cyra\cyrk\cyrt\cyri\cyrk\cyri: \@practtype\\
    \cyrk\cyra\cyrf\cyre\cyrd\cyrr\cyra: \@chair\\
    \cyrk\cyru\cyrr\cyrs: \@course\\
    \cyrs\cyre\cyrm\cyre\cyrs\cyrt\cyrr: \@term\\
    \cyrp\cyrr\cyro\cyrd\cyro\cyrl\cyrzh\cyri\cyrt\cyre\cyrl\cyrsftsn\cyrn%
    \cyro\cyrs\cyrt\cyrsftsn: \@duration\ \cyrn\cyre\cyrd., \cyrs\ \@practStart\ \cyrg. \cyrp\cyro\ \@practFinish\ \cyrg.
\end{flushleft}
%\parindent=-0.2cm
\vspace{1cm}

\noindent
\CYRR\cyru\cyrk\cyro\cyrv\cyro\cyrd\cyri\cyrt\cyre\cyrl\cyrsftsn\ \cyrp%
\cyrr\cyra\cyrk\cyrt\cyri\cyrk\cyri\ \cyro\cyrt\ \cyru\cyrn\cyri\cyrv%
\cyre\cyrr\cyrs\cyri\cyrt\cyre\cyrt\cyra,\\[12pt]%
\signature{\@satitle}{\@saname}\\[14pt]
\CYRR\cyru\cyrk\cyro\cyrv\cyro\cyrd\cyri\cyrt\cyre\cyrl\cyrsftsn\ \cyrp%
\cyrr\cyra\cyrk\cyrt\cyri\cyrk\cyri\ \cyro\cyrt\ \cyro\cyrr\cyrg\cyra%
\cyrn\cyri\cyrz\cyra\cyrc\cyri\cyri\ (\cyru\cyrch\cyrr\cyre\cyrzh\cyrd%
\cyre\cyrn\cyri\cyrya, \cyrp\cyrr\cyre\cyrd\cyrp\cyrr\cyri\cyrya\cyrt%
\cyri\cyrya),\\[12pt]%
\signature{\@patitle}{\@paname}

\newpage
\thispagestyle{empty}
\vspace*{11cm}
\CYRT\cyre\cyrm\cyra\ \cyrp\cyrr\cyra\cyrk\cyrt\cyri\cyrk\cyri:<<\@worktitle>>
\parindent=1.25cm
\newpage
}
% --------------------------------------------------------------------------%


% --------------------------------------------------------------------------%
% Referat title page
% --------------------------------------------------------------------------%
\newcommand{\RefMakeTitle}
{
\thispagestyle{empty}
\shapka

\vspace{3cm}
{\centering
\textbf{\MakeUppercase{\@worktitle}}
\\[0.3cm]
{\@workname}

}

\vspace{1.5cm}
\begin{flushleft}
\@studenttitle\ \@course\ \cyrk\cyru\cyrr\cyrs\cyra\ \@group\ \cyrg%
\cyrr\cyru\cyrp\cyrp\cyrery\\
\@spectype\ \@napravlenie\\
\@department\\
\@studentName
\end{flushleft}
\vfill

\noindent
\CYRP\cyrr\cyro\cyrv\cyre\cyrr\cyri\cyrl\\
\signature{\@satitle}{\@saname}

\vfill
{\centering{\cyr\CYRS\cyra\cyrr\cyra\cyrt\cyro\cyrv\ \@year}

}
\newpage
}
% --------------------------------------------------------------------------%

% --------------------------------------------------------------------------%
% Last page
% --------------------------------------------------------------------------%
\newcommand{\lastpage}
{
\newpage
\thispagestyle{empty}
\vspace*{11cm}
\@worktype\ <<\@worktitle>>\ \@typework\ \cyrm\cyrn\cyro\cyrishrt\ %
\cyrs\cyra\cyrm\cyro\cyrs\cyrt\cyro\cyrya\cyrt\cyre\cyrl\cyrsftsn\cyrn%
\cyro, \cyri\ \cyrn\cyra\ \cyrv\cyrs\cyre\ \cyri\cyrs\cyrt\cyro\cyrch%
\cyrn\cyri\cyrk\cyri, \cyri\cyrm\cyre\cyryu\cyrshch\cyri\cyre\cyrs%
\cyrya\ \cyrv\ \cyrr\cyra\cyrb\cyro\cyrt\cyre, \cyrd\cyra\cyrn\cyrery\ %
\cyrs\cyro\cyro\cyrt\cyrv\cyre\cyrs\cyrt\cyrv\cyru\cyryu\cyrshch\cyri%
\cyre\ \cyrs\cyrs\cyrery\cyrl\cyrk\cyri.\par
\parindent=9cm
\parbox{8cm}{
\begin{flushleft}
\hbox to 6cm{\hbox to 3.5cm{\hrulefill}/\hbox to 3.5cm{\hrulefill}/}
\end{flushleft}
}
}


% --------------------------------------------------------------------------%
% enumerations
% --------------------------------------------------------------------------%
\renewcommand\theenumi  {\@arabic\c@enumi}
\renewcommand\theenumii {\@asbuk\c@enumii}
\renewcommand\theenumiii{\@roman\c@enumiii}
\renewcommand\theenumiv {\@Asbuk\c@enumiv}
\newcommand\atheenumi{\@asbuk\c@enumi}
\newcommand\atheenumii{\@asbuk\c@enumii}
\renewcommand\labelenumi  {\theenumi.}
\renewcommand\labelenumii {\theenumii.}
\renewcommand\labelenumiii{\theenumiii.}
\renewcommand\labelenumiv {\theenumiv.}
\renewcommand\p@enumii  {\theenumi}
\renewcommand\p@enumiii {\theenumi.\theenumii}
\renewcommand\p@enumiv  {\p@enumiii.\theenumiii}
\renewcommand\labelitemi  {\normalfont\bfseries\textemdash}
\renewcommand\labelitemii {\normalfont\bfseries\textendash}
\renewcommand\labelitemiii{\textperiodcentered}
\renewcommand\labelitemiv {\textasteriskcentered}

\renewcommand{\@listI}{%
\leftmargin=52pt
\rightmargin=0pt
\labelsep=7pt
\labelwidth=20pt
\itemindent=0pt
\listparindent=0pt
\topsep=4pt plus 2pt minus 4pt
\partopsep=0pt plus 1pt minus 1pt
\parsep=0pt plus 1pt
\itemsep=\parsep}
% --------------------------------------------------------------------------%


% --------------------------------------------------------------------------%
% References
% --------------------------------------------------------------------------%
\makeatletter
\def\@biblabel#1{#1 }

\renewenvironment{thebibliography}[1]
{
  \starsection{\cyr\CYRS\CYRP\CYRI\CYRS\CYRO\CYRK\ \CYRI\CYRS\CYRP\CYRO\CYRL%
  \CYRSFTSN\CYRZ\CYRO\CYRV\CYRA\CYRN\CYRN\CYRERY\CYRH\ \CYRI\CYRS\CYRT%
  \CYRO\CYRCH\CYRN\CYRI\CYRK\CYRO\CYRV}
  \list{\@biblabel{\@arabic\c@enumiv}}%
  {\settowidth\labelwidth{\@biblabel{#1}}%
    \leftmargin\labelwidth
    \advance\leftmargin\labelsep
    \setlength{\itemsep}{0pt}
    \@openbib@code
    \usecounter{enumiv}%
    \let\p@enumiv\@empty
    \renewcommand\theenumiv{\@arabic\c@enumiv}}%
  \sloppy
  \clubpenalty4000
  \@clubpenalty \clubpenalty
  \widowpenalty4000%
  \sfcode`\.\@m}
{\def\@noitemerr
  {\@latex@warning{Empty `thebibliography' environment}}%
  \endlist}

\makeatother
% --------------------------------------------------------------------------%
