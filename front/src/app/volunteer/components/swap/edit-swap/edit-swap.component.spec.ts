import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditSwapComponent } from './edit-swap.component';

describe('EditSwapComponent', () => {
  let component: EditSwapComponent;
  let fixture: ComponentFixture<EditSwapComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EditSwapComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EditSwapComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
