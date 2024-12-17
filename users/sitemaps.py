from django.contrib.sitemaps import Sitemap
from django.urls import reverse





class StatisticSitemap( Sitemap ):
      
      def items( self ):
            return [
                  'home',
            ]
      
      
      
      def location( self, item ):
            return reverse( item )





class CategorySitemap( Sitemap ):
      
      def items( self ):
            pass
            # return Tag.objects.all()    # this would give back all the categories of the Tag-table
            # in order for this to work we will need the method `get_absolute_url` defined in the
            # Tag-Class-Model like:
      
      # in class Category
      # def get_absolute_url( self ):
      #     return f'/category/{self.slug}/'





class PostPagesSitemap( Sitemap ):
      
      def items( self ):
            pass
            # return Post.objects.all()[:100]   # This will give back a return of the latest 100 Posts in the DB
      
      # in class Post:
      # def get_absolute_url( self ):
      #     return f'/post/{self.id}/'
      
      
