"""
This focus is to apply one of many design patterns under behavioural called strateg to handling the sorting of josb to be showing
the most recent added roles 
"""

class SortStrategy:
     def sort(self, queryset):
          raise NotImplementedError("The Subclasses must implement this method")
     
class SortRecent(SortStrategy):
     def sort(self, queryset):
          return queryset.order_by('-posted_date')

class SortOldest(SortStrategy):
     def sort(self, queryset):
          return queryset.order_by('posted_date')