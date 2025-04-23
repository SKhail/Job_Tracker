"""
Will move the filtering feature in its own file to promote Single Responbility and good practive. This isolating will help
for testing later on and reduce errors occuring 
"""
class StatusFilter:
   def apply(self, queryset, request):
      status = request.GET.get('status')
      if status:
         return queryset.filter(status=status)
      return queryset