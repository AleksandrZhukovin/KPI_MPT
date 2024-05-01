--[[
В Lua всі об'єкти зберігаються на кучі і не можливо контролювати вручну
де буде створюватись новий об'єк, на кучі чи стеку
--]]

describe("Lua Object Creation on Heap Test", function()
    it("Should demonstrate object creation on the heap", function()
        local obj = {
            value = 10,
            increment = function(self)
                self.value = self.value + 1
            end,
            getValue = function(self)
                return self.value
            end
        }

        assert.is_equal(obj:getValue(), 10)

        obj:increment()

        assert.is_equal(obj:getValue(), 11)
    end)
end)