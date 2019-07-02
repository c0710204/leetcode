class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Given an absolute path for a file (Unix-style), simplify it. Or in other
        words, convert it to the canonical path.

        In a UNIX-style file system, a period . refers to the current directory.
        Furthermore, a double period .. moves the directory up a level. For more
        information, see: Absolute path vs relative path in Linux/Unix

        Note that the returned canonical path must always begin with a slash /,
        and there must be only a single slash / between two directory names. The
        last directory name (if it exists) must not end with a trailing /. Also,
        the canonical path must be the shortest string representing the absolute path.
        """
        #side case
        if path=="/":
          return "/"
        #init
        result_str_compents=[]
        i=0
        #code
        source_str_compents=path.split('/')
        source_str_compents=source_str_compents[1:]
        for i in range(len(source_str_compents)):
          if source_str_compents[i]=="" or source_str_compents[i]==".":
            continue
          if source_str_compents[i]=="..":
            if len(result_str_compents)>0:
              result_str_compents=result_str_compents[:-1]
            continue
          result_str_compents.append(source_str_compents[i])
        return '/'+'/'.join(result_str_compents)

if __name__=="__main__":
  solu=Solution()
  assert(solu.simplifyPath("/home/")=="/home")
  assert(solu.simplifyPath("/home/..")=="/")
  assert(solu.simplifyPath("/home/../..")=="/")
  assert(solu.simplifyPath("/home/../../sss")=="/sss")